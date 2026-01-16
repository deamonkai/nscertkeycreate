import json

import responses

from certctl.scripts import nsconsole_deploy


def _args(args):
    return nsconsole_deploy.build_arg_parser().parse_args(args)


@responses.activate
def test_list_adc_json(tmp_path, monkeypatch):
    base = "https://console.example"
    monkeypatch.setenv("CERTCTL_CONSOLE_PASSWORD", "secret")

    responses.add(
        responses.POST,
        f"{base}/nitro/v2/config/login",
        json={"login": [{"sessionid": "token"}]},
        status=200,
    )
    responses.add(
        responses.GET,
        f"{base}/nitro/v2/config/managed_device",
        json={
            "errorcode": 0,
            "managed_device": [
                {
                    "id": "1",
                    "display_name": "adc-1",
                    "ip_address": "10.0.0.1",
                    "device_family": "NetScaler",
                    "ha_master_state": "Primary",
                },
                {
                    "id": "2",
                    "display_name": "adc-2",
                    "ip_address": "10.0.0.2",
                    "device_family": "NetScaler",
                    "ha_master_state": "Secondary",
                },
            ],
        },
        status=200,
    )

    out_path = tmp_path / "devices.json"
    args = _args(
        [
            "--console",
            base,
            "--user",
            "nsroot",
            "--certkeypair",
            "ignored",
            "--list-adc",
            "json",
            "--list-adc-out",
            str(out_path),
        ]
    )
    assert nsconsole_deploy.run(args) == 0

    data = json.loads(out_path.read_text(encoding="utf-8"))
    assert data[0]["ip_address"] == "10.0.0.1"
    assert all(row["ha_master_state"] != "Secondary" for row in data)
