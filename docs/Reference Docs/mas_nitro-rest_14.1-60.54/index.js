rdx.views =
{
    header_view:
    {
        type: rdx.view_constants.HEADER_VIEW,
        view_properties: {"stand_alone": true, brand_value: "NetScaler Console NITRO API Documentation"}
    }
};

rdx.page.add_event_handler(rdx.events.APP_LOADED, new rdx.callback(function() {
    rdx.images.COMPANY_LOGO_IMG = "rdx/images/company_logo.png";
    //Hack to avoid showing status bar
    rdx.status_bar._status = $("<div>");
}));

rdx.page.add_event_handler(rdx.events.PAGE_LOADED, new rdx.callback(null, function() {
    //Hack to show build info on the top-right corner of header
	var build_value = "("+version+": " + "Build " +build+")";
    $(".ns_logo_version").append($("<span>").addClass("build_version").append(build_value));

    var tree_nodes =
    [
		new rdx.tree_node({
            name: "Introduction",
            view:
            {
                type: rdx.view_constants.URL_VIEW,
                url: "doc/getting_started_guide_rest.pdf"
            },
            nodes:
            [
            	new rdx.tree_node({
								name: "Getting Started Guide",
								view:
								{
									type: rdx.view_constants.URL_VIEW,
									url: "doc/getting_started_guide_rest.pdf"
					}}),
				new rdx.tree_node({
					name: "Configuration",
					view:
					{
						type: rdx.view_constants.URL_VIEW,
						url: "configuration.html"
					},
					nodes :
						[
						
								new rdx.tree_node({
									name: "Analytics",
									view:
									{
										type: rdx.view_constants.URL_VIEW,
										url: "html/config_list_analytics_v2.html"
									},
									nodes: 
										[
											new rdx.tree_node({
												name: "Common Resources",
												view:
												{
													type: rdx.view_constants.URL_VIEW,
													url: "html/config_list_analytics_common_resrc_v2.html"
												},
												nodes : config_tree_nodes_analytics_common_resrc_v2
											}),
											new rdx.tree_node({
												name: "Gateway Insight",
												view:
												{
													type: rdx.view_constants.URL_VIEW,
													url: "html/config_list_analytics_gateway_insight_v2.html"
												},
												nodes : config_tree_nodes_analytics_gateway_insight_v2
											}),
											new rdx.tree_node({
												name: "HDX Insight",
												view:
												{
													type: rdx.view_constants.URL_VIEW,
													url: "html/config_list_analytics_hdx_insight_v2.html"
												},
												nodes : config_tree_nodes_analytics_hdx_insight_v2
											}),
											new rdx.tree_node({
												name: "Security Insight",
												view:
												{
													type: rdx.view_constants.URL_VIEW,
													url: "html/config_list_analytics_security_insight_v2.html"
												},
												nodes : config_tree_nodes_analytics_security_insight_v2
											}),
											new rdx.tree_node({
												name: "TCP Insight",
												view:
												{
													type: rdx.view_constants.URL_VIEW,
													url: "html/config_list_analytics_tcp_insight_v2.html"
												},
												nodes : config_tree_nodes_analytics_tcp_insight_v2
											}),
											new rdx.tree_node({
												name: "Video Insight",
												view:
												{
													type: rdx.view_constants.URL_VIEW,
													url: "html/config_list_analytics_video_insight_v2.html"
												},
												nodes : config_tree_nodes_analytics_video_insight_v2
											}),
											new rdx.tree_node({
												name: "WAN Insight",
												view:
												{
													type: rdx.view_constants.URL_VIEW,
													url: "html/config_list_analytics_wan_insight_v2.html"
												},
												nodes : config_tree_nodes_analytics_wan_insight_v2
											}),
											new rdx.tree_node({
												name: "Web Insight",
												view:
												{
													type: rdx.view_constants.URL_VIEW,
													url: "html/config_list_analytics_web_insight_v2.html"
												},
												nodes : config_tree_nodes_analytics_web_insight_v2
											})
										]
								}),
								new rdx.tree_node({
									name: "Applications",
									view:
									{
										type: rdx.view_constants.URL_VIEW,
										url: "html/config_list_applications_v2.html"
									},
									nodes: config_tree_nodes_applications_v2
								}),
								new rdx.tree_node({
									name: "Configuration Audit",
									view:
									{
										type: rdx.view_constants.URL_VIEW,
										url: "html/config_list_config_audit_v2.html"
									},
									nodes: config_tree_nodes_config_audit_v2
								}),
								new rdx.tree_node({
									name: "Configuration Jobs",
									view:
									{
										type: rdx.view_constants.URL_VIEW,
										url: "html/config_list_config_jobs_v2.html"
									},
									nodes: config_tree_nodes_config_jobs_v2
								}),
								new rdx.tree_node({
									name: "Device SSL Certificates",
									view:
									{
										type: rdx.view_constants.URL_VIEW,
										url: "html/config_list_device_ssl_certs_v2.html"
									},
									nodes: config_tree_nodes_device_ssl_certs_v2
								}),
								new rdx.tree_node({
									name: "Events",
									view:
									{
										type: rdx.view_constants.URL_VIEW,
										url: "html/config_list_events_v2.html"
									},
									nodes: config_tree_nodes_events_v2
								}),
								new rdx.tree_node({
									name: "Instances",
									view:
									{
										type: rdx.view_constants.URL_VIEW,
										url: "html/config_list_instances_v2.html"
									},
									nodes: 
										[
											new rdx.tree_node({
												name: "Common Resources",
												view:
												{
													type: rdx.view_constants.URL_VIEW,
													url: "html/config_list_instances_common_resrc_v2.html"
												},
												nodes : config_tree_nodes_instances_common_resrc_v2
											}),
											new rdx.tree_node({
												name: "HAProxy",
												view:
												{
													type: rdx.view_constants.URL_VIEW,
													url: "html/config_list_instances_haproxy_v2.html"
												},
												nodes : config_tree_nodes_instances_haproxy_v2
											}),
											new rdx.tree_node({
												name: "NetScaler",
												view:
												{
													type: rdx.view_constants.URL_VIEW,
													url: "html/config_list_instances_ns_mpx_vpx_v2.html"
												},
												nodes : config_tree_nodes_instances_ns_mpx_vpx_v2
											}),
											new rdx.tree_node({
												name: "NetScaler SDX",
												view:
												{
													type: rdx.view_constants.URL_VIEW,
													url: "html/config_list_instances_ns_sdx_v2.html"
												},
												nodes : config_tree_nodes_instances_ns_sdx_v2
											})
										]
								}),
								new rdx.tree_node({
									name: "Licenses",
									view:
									{
										type: rdx.view_constants.URL_VIEW,
										url: "html/config_list_licenses_v2.html"
									},
									nodes: config_tree_nodes_licenses_v2
								}),
								new rdx.tree_node({
									name: "Network Functions",
									view:
									{
										type: rdx.view_constants.URL_VIEW,
										url: "html/config_list_network_functions_v2.html"
									},
									nodes: 
										[
											new rdx.tree_node({
												name: "Authentication",
												view:
												{
													type: rdx.view_constants.URL_VIEW,
													url: "html/config_list_network_functions_authentication_v2.html"
												},
												nodes : config_tree_nodes_network_functions_authentication_v2
											}),
											new rdx.tree_node({
												name: "Cache Redirection",
												view:
												{
													type: rdx.view_constants.URL_VIEW,
													url: "html/config_list_network_functions_cache_redirection_v2.html"
												},
												nodes : config_tree_nodes_network_functions_cache_redirection_v2
											}),
											new rdx.tree_node({
												name: "Common Resources",
												view:
												{
													type: rdx.view_constants.URL_VIEW,
													url: "html/config_list_network_functions_common_resrc_v2.html"
												},
												nodes : config_tree_nodes_network_functions_common_resrc_v2
											}),
											new rdx.tree_node({
												name: "Content Switching",
												view:
												{
													type: rdx.view_constants.URL_VIEW,
													url: "html/config_list_network_functions_content_switching_v2.html"
												},
												nodes : config_tree_nodes_network_functions_content_switching_v2
											}),
											new rdx.tree_node({
												name: "GSLB",
												view:
												{
													type: rdx.view_constants.URL_VIEW,
													url: "html/config_list_network_functions_gslb_v2.html"
												},
												nodes : config_tree_nodes_network_functions_gslb_v2
											}),
											new rdx.tree_node({
												name: "HAProxy",
												view:
												{
													type: rdx.view_constants.URL_VIEW,
													url: "html/config_list_network_functions_haproxy_v2.html"
												},
												nodes : config_tree_nodes_network_functions_haproxy_v2
											}),
											new rdx.tree_node({
												name: "Load Balancing",
												view:
												{
													type: rdx.view_constants.URL_VIEW,
													url: "html/config_list_network_functions_load_balancing_v2.html"
												},
												nodes : config_tree_nodes_network_functions_load_balancing_v2
											}),
											new rdx.tree_node({
												name: "NetScaler Gateway",
												view:
												{
													type: rdx.view_constants.URL_VIEW,
													url: "html/config_list_network_functions_ns_gateway_v2.html"
												},
												nodes : config_tree_nodes_network_functions_ns_gateway_v2
											})
										]
								}),
								new rdx.tree_node({
									name: "Network Reporting",
									view:
									{
										type: rdx.view_constants.URL_VIEW,
										url: "html/config_list_network_reporting_v2.html"
									},
									nodes: config_tree_nodes_network_reporting_v2
								}),
								new rdx.tree_node({
									name: "Orchestration",
									view:
									{
										type: rdx.view_constants.URL_VIEW,
										url: "html/config_list_orchestration_v2.html"
									},
									nodes: 
										[
											new rdx.tree_node({
												name: "Admin",
												view:
												{
													type: rdx.view_constants.URL_VIEW,
													url: "html/config_list_orchestration_admin_v2.html"
												},
												nodes : config_tree_nodes_orchestration_admin_v2
											}),
											new rdx.tree_node({
												name: "Common",
												view:
												{
													type: rdx.view_constants.URL_VIEW,
													url: "html/config_list_orchestration_common_v2.html"
												},
												nodes : config_tree_nodes_orchestration_common_v2
											}),
											new rdx.tree_node({
												name: "Openstack",
												view:
												{
													type: rdx.view_constants.URL_VIEW,
													url: "html/config_list_orchestration_openstack_v2.html"
												},
												nodes : config_tree_nodes_orchestration_openstack_v2
											})
										]
								}),
								new rdx.tree_node({
									name: "Stylebooks",
									view:
									{
										type: rdx.view_constants.URL_VIEW,
										url: "html/config_list_stylebooks_v2.html"
									},
									nodes: config_tree_nodes_stylebooks_v2
								}),								
								new rdx.tree_node({
									name: "System",
									view:
									{
										type: rdx.view_constants.URL_VIEW,
										url: "html/config_list_system_v2.html"
									},
									nodes: config_tree_nodes_system_v2
								}),
								new rdx.tree_node({
									name: "Tools",
									view:
									{
										type: rdx.view_constants.URL_VIEW,
										url: "html/config_list_tools_v2.html"
									},
									nodes: config_tree_nodes_tools_v2
								})
					]
				}),
				new rdx.tree_node({
					name: "Appendix",
					view:
					{
						type: rdx.view_constants.URL_VIEW,
						url: "doc/errorlisting.html"
					},
					nodes:
					[
						new rdx.tree_node({
							name: "Error Messages",
							view:
							{
								type: rdx.view_constants.URL_VIEW,
								url: "doc/errorlisting.html"
							}
						})
					]
				})
            ]
        })

  ];
    var tree = new rdx.tree(rdx.page.get_content(), tree_nodes, {tree_pane_min_width: 260, show_expand_collapse_all: true});
    tree.render();
    //Hack to not show bread crumbs (as it works unexpectedly)
    $(".title_tool_bar_table").hide();
}));