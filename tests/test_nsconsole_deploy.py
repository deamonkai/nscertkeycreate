import responses

from certctl.scripts import nsconsole_deploy


def _args(args):
    return nsconsole_deploy.build_arg_parser().parse_args(args)


def _add_login(resps, base):
    resps.add(
        responses.POST,
        f"{base}/nitro/v2/config/login",
        json={"login": [{"sessionid": "token"}]},
        status=200,
    )


def _add_certkey(resps, base, name, binding):
    resps.add(
        responses.GET,
        f"{base}/nitro/v2/config/ns_ssl_certkey",
        match=[responses.matchers.query_param_matcher({"filter": f"certkeypair_name:{name}"})],
        json={
            "errorcode": 0,
            "ns_ssl_certkey": [{"certkeypair_name": name, "id": "cert-id", "entity_binding_arr": [binding]}],
        },
        status=200,
    )


@responses.activate
def test_deploy_binds_and_links(tmp_path, monkeypatch):
    base = "https://console.example"
    monkeypatch.setenv("CERTCTL_CONSOLE_PASSWORD", "secret")

    _add_login(responses, base)
    _add_certkey(responses, base, "target", {"certkeypair_name": "old", "ns_ip_address": "10.0.0.1", "id": "123"})

    responses.add(
        responses.POST,
        f"{base}/nitro/v2/config/ns_ssl_certkey",
        json={"errorcode": 0, "message": "Done"},
        status=200,
    )
    responses.add(
        responses.POST,
        f"{base}/nitro/v2/config/ns_ssl_certlink",
        json={"errorcode": 0, "message": "Done"},
        status=200,
    )

    args = _args(
        [
            "--console",
            base,
            "--user",
            "nsroot",
            "--certkeypair",
            "target",
            "--ca-certkey",
            "root_ca",
        ]
    )
    assert nsconsole_deploy.run(args) == 0

    assert any("action=bind_cert" in call.request.url for call in responses.calls)
    assert any("action=link" in call.request.url for call in responses.calls)


@responses.activate
def test_deploy_links_from_chain(tmp_path, monkeypatch):
    base = "https://console.example"
    monkeypatch.setenv("CERTCTL_CONSOLE_PASSWORD", "secret")

    _add_login(responses, base)
    responses.add(
        responses.GET,
        f"{base}/nitro/v2/config/ns_ssl_certkey",
        match=[responses.matchers.query_param_matcher({"filter": "certkeypair_name:source"})],
        json={
            "errorcode": 0,
            "ns_ssl_certkey": [
                {
                    "certkeypair_name": "source",
                    "entity_binding_arr": [{"ns_ip_address": "10.0.0.1", "id": "123"}],
                    "certkeychain": [{"cert_name": "root_ca"}],
                }
            ],
        },
        status=200,
    )
    responses.add(
        responses.GET,
        f"{base}/nitro/v2/config/ns_ssl_certkey",
        match=[responses.matchers.query_param_matcher({"filter": "certkeypair_name:target"})],
        json={"errorcode": 0, "ns_ssl_certkey": [{"certkeypair_name": "target", "id": "target-id"}]},
        status=200,
    )
    responses.add(
        responses.POST,
        f"{base}/nitro/v2/config/ns_ssl_certkey",
        json={"errorcode": 0, "message": "Done"},
        status=200,
    )
    responses.add(
        responses.POST,
        f"{base}/nitro/v2/config/ns_ssl_certlink",
        json={"errorcode": 0, "message": "Done"},
        status=200,
    )

    args = _args(
        [
            "--console",
            base,
            "--user",
            "nsroot",
            "--certkeypair",
            "target",
            "--source-certkeypair",
            "source",
        ]
    )
    assert nsconsole_deploy.run(args) == 0
    assert any("action=link" in call.request.url for call in responses.calls)


@responses.activate
def test_deploy_falls_back_to_modify(monkeypatch):
    base = "https://console.example"
    monkeypatch.setenv("CERTCTL_CONSOLE_PASSWORD", "secret")

    _add_login(responses, base)
    _add_certkey(responses, base, "target", {"certkeypair_name": "old", "ns_ip_address": "10.0.0.1", "id": "123"})

    responses.add(
        responses.POST,
        f"{base}/nitro/v2/config/ns_ssl_certkey",
        json={"message": "API not supported in this deployment"},
        status=405,
    )
    responses.add(
        responses.PUT,
        f"{base}/nitro/v2/config/ns_ssl_certkey/cert-id",
        json={"errorcode": 0, "message": "Done"},
        status=200,
    )

    args = _args(
        [
            "--console",
            base,
            "--user",
            "nsroot",
            "--certkeypair",
            "target",
            "--no-link-ca",
        ]
    )
    assert nsconsole_deploy.run(args) == 0
    assert any(call.request.method == "PUT" for call in responses.calls)


@responses.activate
def test_deploy_resolves_cn(monkeypatch):
    base = "https://console.example"
    monkeypatch.setenv("CERTCTL_CONSOLE_PASSWORD", "secret")

    _add_login(responses, base)
    responses.add(
        responses.GET,
        f"{base}/nitro/v2/config/ns_ssl_certkey",
        match=[responses.matchers.query_param_matcher({"filter": "certkeypair_name:test.molloyhome.net"})],
        json={"errorcode": 0, "ns_ssl_certkey": []},
        status=200,
    )
    responses.add(
        responses.GET,
        f"{base}/nitro/v2/config/ns_ssl_certkey",
        match=[responses.matchers.query_param_matcher({"pagesize": "200"})],
        json={
            "errorcode": 0,
            "ns_ssl_certkey": [
                {
                    "certkeypair_name": "test_molloyhome_net",
                    "id": "cert-id",
                    "subject": "CN=test.molloyhome.net, O=Example",
                    "entity_binding_arr": [{"certkeypair_name": "old", "ns_ip_address": "10.0.0.1", "id": "123"}],
                }
            ],
        },
        status=200,
    )
    responses.add(
        responses.POST,
        f"{base}/nitro/v2/config/ns_ssl_certkey",
        json={"message": "API not supported in this deployment"},
        status=405,
    )
    responses.add(
        responses.PUT,
        f"{base}/nitro/v2/config/ns_ssl_certkey/cert-id",
        json={"errorcode": 0, "message": "Done"},
        status=200,
    )

    args = _args(
        [
            "--console",
            base,
            "--user",
            "nsroot",
            "--certkeypair",
            "test.molloyhome.net",
            "--no-link-ca",
        ]
    )
    assert nsconsole_deploy.run(args) == 0


@responses.activate
def test_deploy_syncs_inventory(monkeypatch):
    base = "https://console.example"
    monkeypatch.setenv("CERTCTL_CONSOLE_PASSWORD", "secret")

    _add_login(responses, base)
    responses.add(
        responses.GET,
        f"{base}/nitro/v2/config/ns_ssl_certkey",
        match=[responses.matchers.query_param_matcher({"filter": "certkeypair_name:target"})],
        json={"errorcode": 0, "ns_ssl_certkey": []},
        status=200,
    )
    responses.add(
        responses.POST,
        f"{base}/nitro/v2/config/ns_ssl_certkey",
        match=[responses.matchers.query_param_matcher({"action": "inventory"})],
        json={"errorcode": 0, "message": "Done"},
        status=200,
    )
    responses.add(
        responses.GET,
        f"{base}/nitro/v2/config/ns_ssl_certkey",
        match=[responses.matchers.query_param_matcher({"filter": "certkeypair_name:target"})],
        json={
            "errorcode": 0,
            "ns_ssl_certkey": [
                {
                    "certkeypair_name": "target",
                    "id": "cert-id",
                    "entity_binding_arr": [{"certkeypair_name": "old", "ns_ip_address": "10.0.0.1", "id": "123"}],
                }
            ],
        },
        status=200,
    )
    responses.add(
        responses.POST,
        f"{base}/nitro/v2/config/ns_ssl_certkey",
        json={"message": "API not supported in this deployment"},
        status=405,
    )
    responses.add(
        responses.PUT,
        f"{base}/nitro/v2/config/ns_ssl_certkey/cert-id",
        json={"errorcode": 0, "message": "Done"},
        status=200,
    )

    args = _args(
        [
            "--console",
            base,
            "--user",
            "nsroot",
            "--certkeypair",
            "target",
            "--sync",
            "--no-link-ca",
        ]
    )
    assert nsconsole_deploy.run(args) == 0


@responses.activate
def test_deploy_imports_missing_from_adc(monkeypatch):
    base = "https://console.example"
    monkeypatch.setenv("CERTCTL_CONSOLE_PASSWORD", "secret")

    _add_login(responses, base)
    responses.add(
        responses.GET,
        f"{base}/nitro/v2/config/ns_ssl_certkey",
        match=[responses.matchers.query_param_matcher({"filter": "certkeypair_name:test.molloyhome.net"})],
        json={"errorcode": 0, "ns_ssl_certkey": []},
        status=200,
    )
    responses.add(
        responses.POST,
        f"{base}/nitro/v2/config/ns_ssl_certkey",
        match=[responses.matchers.query_param_matcher({"action": "list_entity_cert"})],
        json={
            "errorcode": 0,
            "ns_ssl_certkey": [
                {
                    "certkeypair_name": "test_molloyhome_net",
                    "subject": "CN=test.molloyhome.net, O=Example",
                }
            ],
        },
        status=200,
    )
    responses.add(
        responses.POST,
        f"{base}/nitro/v2/config/ns_ssl_certkey",
        json={"errorcode": 0, "message": "Done"},
        status=200,
    )
    responses.add(
        responses.GET,
        f"{base}/nitro/v2/config/ns_ssl_certkey",
        match=[responses.matchers.query_param_matcher({"filter": "certkeypair_name:test.molloyhome.net"})],
        json={
            "errorcode": 0,
            "ns_ssl_certkey": [
                {
                    "certkeypair_name": "test.molloyhome.net",
                    "id": "cert-id",
                    "entity_binding_arr": [{"certkeypair_name": "old", "ns_ip_address": "10.0.0.1", "id": "123"}],
                }
            ],
        },
        status=200,
    )
    responses.add(
        responses.POST,
        f"{base}/nitro/v2/config/ns_ssl_certkey",
        json={"message": "API not supported in this deployment"},
        status=405,
    )
    responses.add(
        responses.PUT,
        f"{base}/nitro/v2/config/ns_ssl_certkey/cert-id",
        json={"errorcode": 0, "message": "Done"},
        status=200,
    )

    args = _args(
        [
            "--console",
            base,
            "--user",
            "nsroot",
            "--certkeypair",
            "test.molloyhome.net",
            "--import-missing",
            "--adc-ip",
            "10.0.0.1",
            "--no-link-ca",
        ]
    )
    assert nsconsole_deploy.run(args) == 0


@responses.activate
def test_deploy_imports_missing_with_guess_on_unsupported_list(monkeypatch):
    base = "https://console.example"
    monkeypatch.setenv("CERTCTL_CONSOLE_PASSWORD", "secret")

    _add_login(responses, base)
    responses.add(
        responses.GET,
        f"{base}/nitro/v2/config/ns_ssl_certkey",
        match=[responses.matchers.query_param_matcher({"filter": "certkeypair_name:test.molloyhome.net"})],
        json={"errorcode": 0, "ns_ssl_certkey": []},
        status=200,
    )
    responses.add(
        responses.POST,
        f"{base}/nitro/v2/config/ns_ssl_certkey",
        match=[responses.matchers.query_param_matcher({"action": "list_entity_cert"})],
        json={"message": "API not supported in this deployment"},
        status=405,
    )
    responses.add(
        responses.POST,
        f"{base}/nitro/v2/config/ns_ssl_certkey",
        json={"errorcode": 0, "message": "Done"},
        status=200,
    )
    responses.add(
        responses.GET,
        f"{base}/nitro/v2/config/ns_ssl_certkey",
        match=[responses.matchers.query_param_matcher({"filter": "certkeypair_name:test.molloyhome.net"})],
        json={
            "errorcode": 0,
            "ns_ssl_certkey": [
                {
                    "certkeypair_name": "test.molloyhome.net",
                    "id": "cert-id",
                    "entity_binding_arr": [{"certkeypair_name": "old", "ns_ip_address": "10.0.0.1", "id": "123"}],
                }
            ],
        },
        status=200,
    )
    responses.add(
        responses.POST,
        f"{base}/nitro/v2/config/ns_ssl_certkey",
        json={"message": "API not supported in this deployment"},
        status=405,
    )
    responses.add(
        responses.PUT,
        f"{base}/nitro/v2/config/ns_ssl_certkey/cert-id",
        json={"errorcode": 0, "message": "Done"},
        status=200,
    )

    args = _args(
        [
            "--console",
            base,
            "--user",
            "nsroot",
            "--certkeypair",
            "test.molloyhome.net",
            "--import-missing",
            "--adc-ip",
            "10.0.0.1",
            "--no-link-ca",
        ]
    )
    assert nsconsole_deploy.run(args) == 0


@responses.activate
def test_deploy_polls_adcs(monkeypatch):
    base = "https://console.example"
    monkeypatch.setenv("CERTCTL_CONSOLE_PASSWORD", "secret")

    _add_login(responses, base)
    responses.add(
        responses.GET,
        f"{base}/nitro/v2/config/managed_device",
        json={
            "errorcode": 0,
            "managed_device": [
                {
                    "id": "dev-1",
                    "display_name": "adc-1",
                    "ip_address": "10.0.0.1",
                    "ha_master_state": "Primary",
                }
            ],
        },
        status=200,
    )
    responses.add(
        responses.POST,
        f"{base}/nitro/v2/config/ns_ssl_certkey_policy",
        match=[responses.matchers.query_param_matcher({"action": "do_poll"})],
        json={"errorcode": 0, "message": "Done"},
        status=200,
    )
    _add_certkey(responses, base, "target", {"certkeypair_name": "old", "ns_ip_address": "10.0.0.1", "id": "123"})
    responses.add(
        responses.POST,
        f"{base}/nitro/v2/config/ns_ssl_certkey",
        json={"errorcode": 0, "message": "Done"},
        status=200,
    )

    args = _args(
        [
            "--console",
            base,
            "--user",
            "nsroot",
            "--certkeypair",
            "target",
            "--list-adc",
            "menu",
            "--poll-adc",
            "--no-link-ca",
        ]
    )
    monkeypatch.setattr("builtins.input", lambda _: "1")
    assert nsconsole_deploy.run(args) == 0
