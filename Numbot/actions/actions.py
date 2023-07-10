from typing import Any, Text, Dict, List
import base64
import time
import os
import json
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.events import SlotSet, FollowupAction
from rasa_sdk import Action, Tracker
from typing import Any, Dict, List, Text
import requests
config2 = {

    "success": True,
    "message": "Successful",
    "data": {
        "layers": [
            {
                "category_id": 790,
                "cat_name": "Fire_station",
                "attributes": [
                    {
                        "col_alias": "fire_stati",
                        "default_dashboard_col": False,
                        "tbl_name": "tbl_fire_station",
                        "col_name": "fire_stati",
                        "type": "distinct"
                    },
                    {
                        "col_alias": "fire_station_name",
                        "default_dashboard_col": False,
                        "tbl_name": "vehicle_info_1",
                        "col_name": "fire_station_name",
                        "type": "distinct"
                    },
                    {
                        "col_alias": "no_of_ambu",
                        "default_dashboard_col": True,
                        "tbl_name": "tbl_fire_station",
                        "col_name": "no_of_ambu",
                        "type": "quantile"
                    },
                    {
                        "col_alias": "no_of_fire",
                        "default_dashboard_col": False,
                        "tbl_name": "tbl_fire_station",
                        "col_name": "no_of_fire",
                        "type": "quantile"
                    },
                    {
                        "col_alias": "vehcl_id",
                        "default_dashboard_col": False,
                        "tbl_name": "vehicle_info_1",
                        "col_name": "vehcl_id",
                        "type": "quantile"
                    }
                ],
                "table_name": "tbl_fire_station",
                "layer_type": "operational"
            },
            {
                "category_id": 791,
                "cat_name": "Road_centerline",
                "attributes": [
                    {
                        "col_alias": "road_name",
                        "default_dashboard_col": False,
                        "tbl_name": "tbl_road_centerline",
                        "col_name": "road_name",
                        "type": "distinct"
                    },
                    {
                        "col_alias": "road_type",
                        "default_dashboard_col": False,
                        "tbl_name": "tbl_road_centerline",
                        "col_name": "road_type",
                        "type": "distinct"
                    },
                    {
                        "col_alias": "road_width",
                        "default_dashboard_col": False,
                        "tbl_name": "tbl_road_centerline",
                        "col_name": "road_width",
                        "type": "quantile"
                    }
                ],
                "table_name": "tbl_road_centerline",
                "layer_type": "operational"
            },
            {
                "category_id": 792,
                "cat_name": "Slum_boundary",
                "attributes": [
                    {
                        "col_alias": "slum_name",
                        "default_dashboard_col": True,
                        "tbl_name": "tbl_slum_boundary",
                        "col_name": "slum_name",
                        "type": "distinct"
                    }
                ],
                "table_name": "tbl_slum_boundary",
                "layer_type": "operational"
            }
        ]
    },
    "funName": "webservice.fn_geoportal_dashboardlayers",
    "funInputs": "133,0,234,25,3,114,74"
}

config1 = {
    "success": True,
    "message": "Successful",
    "data": {
        "map_config": {
            "scale_box": [
                {
                    "zoom_levels": 0,
                    "map_scale": "1:279541132.0143589"
                },
                {
                    "zoom_levels": 1,
                    "map_scale": "1:139770566.00717944"
                },
                {
                    "zoom_levels": 2,
                    "map_scale": "1:69885283.00358972"
                },
                {
                    "zoom_levels": 3,
                    "map_scale": "1:34942641.50179486"
                },
                {
                    "zoom_levels": 4,
                    "map_scale": "1:17471320.75089743"
                },
                {
                    "zoom_levels": 5,
                    "map_scale": "1:8735660.375448715"
                },
                {
                    "zoom_levels": 6,
                    "map_scale": "1:4367830.1877243575"
                },
                {
                    "zoom_levels": 7,
                    "map_scale": "1:2183915.0938621787"
                },
                {
                    "zoom_levels": 8,
                    "map_scale": "1:1091957.5469310894"
                },
                {
                    "zoom_levels": 9,
                    "map_scale": "1:545978.7734655447"
                },
                {
                    "zoom_levels": 10,
                    "map_scale": "1:272989.38673277234"
                },
                {
                    "zoom_levels": 11,
                    "map_scale": "1:136494.69336638617"
                },
                {
                    "zoom_levels": 12,
                    "map_scale": "1:68247.34668319309"
                },
                {
                    "zoom_levels": 13,
                    "map_scale": "1:34123.67334159654"
                },
                {
                    "zoom_levels": 14,
                    "map_scale": "1:17061.83667079827"
                },
                {
                    "zoom_levels": 15,
                    "map_scale": "1:8530.918335399136"
                },
                {
                    "zoom_levels": 16,
                    "map_scale": "1:4265.459167699568"
                },
                {
                    "zoom_levels": 17,
                    "map_scale": "1:2132.729583849784"
                },
                {
                    "zoom_levels": 18,
                    "map_scale": "1:1066.364791924892"
                },
                {
                    "zoom_levels": 19,
                    "map_scale": "1:533.182395962446"
                },
                {
                    "zoom_levels": 20,
                    "map_scale": "1:266.591197981223"
                }
            ],
            "map_center": [
                251666.4211456211,
                2548358.273523046
            ],
            "workspace": "citylayers4",
            "geoserver_url": "http://192.168.10.199/geoserver_new/",
            "prj_id": 74,
            "raster_config": None,
            "map_resolutions": [
                280,
                140,
                70,
                35,
                17.5,
                8.75,
                4.375,
                2.1875,
                1.09375,
                0.546875,
                0.2734375,
                0.13671875,
                0.068359375,
                0.0341796875,
                0.01708984375,
                0.008544921875,
                0.0042724609375,
                0.00213623046875,
                0.001068115234375,
                5.340576171875E-4,
                2.6702880859375E-4
            ],
            "cityname": None,
            "crs_extent": [
                166021.44308053766,
                0,
                9329005.182447437,
                833978.556919458
            ],
            "base_url": "http://192.168.20.56:8020/geoportal/",
            "map_scale": [
                2.795411320143589E8,
                1.3977056600717944E8,
                6.988528300358972E7,
                3.494264150179486E7,
                1.747132075089743E7,
                8735660.375448715,
                4367830.1877243575,
                2183915.0938621787,
                1091957.5469310894,
                545978.7734655447,
                272989.38673277234,
                136494.69336638617,
                68247.34668319309,
                34123.67334159654,
                17061.83667079827,
                8530.918335399136,
                4265.459167699568,
                2132.729583849784,
                1066.364791924892,
                533.182395962446,
                266.591197981223
            ],
            "map_bounds": [
                236612.36672513897,
                2535560.9090531645,
                265754.0956803194,
                2563745.4609238254
            ],
            "project_name": "vmc project",
            "epsg_code": 32643,
            "default_zoom": 0,
            "org_id": 234,
            "min_resolution": 2.6702880859375E-4,
            "app_service_url": "http://192.168.20.56:8020/adminportal/",
            "proj4text": "+proj=utm +zone=43 +datum=WGS84 +units=m +no_defs ",
            "max_resolution": 280,
            "default_raster_id": -1
        },
        "user_config": {
            "pdm_catid": None,
            "user_name": "kushal88",
            "user_types": [
                "dept_admin",
                "dept_admin",
                "dept_admin",
                "dept_admin",
                "dept_admin",
                "app_viewer"
            ],
            "cat_config": {
                "admin": [
                    {
                        "style_conf": [
                            {
                                "style_col_type": "character varying",
                                "col_id": 12773,
                                "filter_type": "string",
                                "style_col_alias": "zone",
                                "style_col_name": "zone"
                            }
                        ],
                        "z_index": 0,
                        "doc_list": None,
                        "user_style_config": [
                            {
                                "interval_count": None,
                                "col_id": None,
                                "sld_name": "234_132_307_ts",
                                "json_value": {
                                    "polygon Geometry": {
                                        "rules": [
                                            {
                                                "symbolizers": [
                                                    {
                                                        "color": "#ea2da6",
                                                        "fillOpacity": 0,
                                                        "outlineWidth": "3",
                                                        "kind": "Fill",
                                                        "graphicFill": {
                                                            "color": "#ea2da6"
                                                        },
                                                        "outlineColor": "#f60000",
                                                        "graphicStroke": {
                                                            "color": "#ea2da6"
                                                        },
                                                        "outlineOpacity": 1
                                                    },
                                                    {
                                                        "labelAllGroup": False,
                                                        "rotate": 0,
                                                        "color": "#000000",
                                                        "offset": [
                                                            0,
                                                            0
                                                        ],
                                                        "kind": "Text",
                                                        "haloColor": "#EEEEEE",
                                                        "label": "label_exp",
                                                        "enabled": False,
                                                        "partials": False,
                                                        "haloWidth": 0,
                                                        "followLine": False,
                                                        "size": 12,
                                                        "opacity": 1,
                                                        "font": [
                                                            "Roboto Light"
                                                        ],
                                                        "group": "no",
                                                        "conflictResolution": False
                                                    }
                                                ],
                                                "scaleDenominator": {
                                                    "min": 0,
                                                    "max": 13
                                                },
                                                "name": "polygon Geometry",
                                                "id": 1
                                            }
                                        ],
                                        "position": 0,
                                        "enabled": True
                                    }
                                },
                                "style_col_alias": None,
                                "style_col_name": None,
                                "style_name": "Untitled Style",
                                "style_type": "admin",
                                "class_type": None,
                                "color_ramp": "OrRd",
                                "is_default_style": True,
                                "filter_type": None,
                                "id": 307
                            }
                        ],
                        "timeseries_config": None,
                        "cat_name": "Vmc_zone",
                        "isthematic": False,
                        "lyr_desc": None,
                        "label_conf": [
                            {
                                "lbl_column_id": 12773,
                                "lbl_column_datatype": "text",
                                "lbl_column_alias": "zone",
                                "lbl_default_col": True
                            }
                        ],
                        "isanimation": False,
                        "table_name": "tbl_vmc_zone",
                        "layer_type": "admin",
                        "category_id": 788,
                        "geom_type": "polygon"
                    },
                    {
                        "style_conf": [
                            {
                                "style_col_type": "numeric",
                                "col_id": 12789,
                                "filter_type": "number",
                                "style_col_alias": "wardno",
                                "style_col_name": "wardno"
                            }
                        ],
                        "z_index": 0,
                        "doc_list": None,
                        "user_style_config": [
                            {
                                "interval_count": None,
                                "col_id": None,
                                "sld_name": "234_132_306_ts",
                                "json_value": {
                                    "polygon Geometry": {
                                        "rules": [
                                            {
                                                "symbolizers": [
                                                    {
                                                        "color": "#e3182b",
                                                        "fillOpacity": 0,
                                                        "outlineWidth": "1",
                                                        "kind": "Fill",
                                                        "graphicFill": {
                                                            "color": "#e3182b"
                                                        },
                                                        "outlineColor": "#c2a2ff",
                                                        "graphicStroke": {
                                                            "color": "#e3182b"
                                                        },
                                                        "outlineOpacity": 1
                                                    },
                                                    {
                                                        "labelAllGroup": False,
                                                        "rotate": 0,
                                                        "color": "#000000",
                                                        "offset": [
                                                            0,
                                                            0
                                                        ],
                                                        "kind": "Text",
                                                        "haloColor": "#EEEEEE",
                                                        "label": "label_exp",
                                                        "enabled": False,
                                                        "partials": False,
                                                        "haloWidth": 0,
                                                        "followLine": False,
                                                        "size": 12,
                                                        "opacity": 1,
                                                        "font": [
                                                            "Roboto Light"
                                                        ],
                                                        "group": "no",
                                                        "conflictResolution": False
                                                    }
                                                ],
                                                "scaleDenominator": {
                                                    "min": 0,
                                                    "max": 13
                                                },
                                                "name": "polygon Geometry",
                                                "id": 1
                                            }
                                        ],
                                        "position": 0,
                                        "enabled": True
                                    }
                                },
                                "style_col_alias": None,
                                "style_col_name": None,
                                "style_name": "Untitled Style",
                                "style_type": "admin",
                                "class_type": None,
                                "color_ramp": "OrRd",
                                "is_default_style": True,
                                "filter_type": None,
                                "id": 306
                            }
                        ],
                        "timeseries_config": None,
                        "cat_name": "Vmc_ward",
                        "isthematic": False,
                        "lyr_desc": None,
                        "label_conf": [
                            {
                                "lbl_column_id": 12789,
                                "lbl_column_datatype": "number",
                                "lbl_column_alias": "wardno",
                                "lbl_default_col": True
                            },
                            {
                                "lbl_column_id": 12787,
                                "lbl_column_datatype": "text",
                                "lbl_column_alias": "name",
                                "lbl_default_col": False
                            }
                        ],
                        "isanimation": False,
                        "table_name": "tbl_vmc_ward",
                        "layer_type": "admin",
                        "category_id": 789,
                        "geom_type": "polygon"
                    }
                ],
                "operational": [
                    {
                        "style_conf": [
                            {
                                "style_col_type": "numeric",
                                "col_id": 12819,
                                "filter_type": "number",
                                "style_col_alias": "total_no_f",
                                "style_col_name": "total_no_f"
                            }
                        ],
                        "z_index": 0,
                        "doc_list": [
                            {
                                "is_popup": True,
                                "is_attribute": True,
                                "text": "Driving License",
                                "doc_id": 59
                            },
                            {
                                "is_popup": True,
                                "is_attribute": False,
                                "text": "bhbh",
                                "doc_id": 113
                            },
                            {
                                "is_popup": True,
                                "is_attribute": True,
                                "text": "aa",
                                "doc_id": 61
                            },
                            {
                                "is_popup": True,
                                "is_attribute": True,
                                "text": "Voting Card",
                                "doc_id": 58
                            },
                            {
                                "is_popup": True,
                                "is_attribute": True,
                                "text": "pancard",
                                "doc_id": 56
                            },
                            {
                                "is_popup": False,
                                "is_attribute": False,
                                "text": "aadhar",
                                "doc_id": 57
                            },
                            {
                                "is_popup": True,
                                "is_attribute": True,
                                "text": "ABC",
                                "doc_id": 96
                            },
                            {
                                "is_popup": True,
                                "is_attribute": True,
                                "text": "aaaa",
                                "doc_id": 60
                            },
                            {
                                "is_popup": True,
                                "is_attribute": True,
                                "text": "XYZ",
                                "doc_id": 95
                            }
                        ],
                        "user_style_config": [
                            {
                                "interval_count": 4,
                                "col_id": 12819,
                                "sld_name": "234_133_395_ts",
                                "json_value": {
                                    "Others": {
                                        "rules": [
                                            {
                                                "filter": [
                                                    "==",
                                                    "style_exp",
                                                    "others"
                                                ],
                                                "symbolizers": [
                                                    {
                                                        "strokeWidth": 3,
                                                        "color": "#67001f",
                                                        "fillOpacity": 1,
                                                        "kind": "Mark",
                                                        "wellKnownName": "Circle",
                                                        "radius": 5,
                                                        "strokeColor": "#555555",
                                                        "strokeOpacity": 1
                                                    },
                                                    {
                                                        "rotate": 0,
                                                        "size": 12,
                                                        "color": "#000000",
                                                        "offset": [
                                                            0,
                                                            0
                                                        ],
                                                        "kind": "Text",
                                                        "haloColor": "#EEEEEE",
                                                        "label": "label_exp",
                                                        "opacity": 1,
                                                        "enabled": False,
                                                        "font": [
                                                            "Roboto Light"
                                                        ],
                                                        "haloWidth": 0
                                                    }
                                                ],
                                                "scaleDenominator": {
                                                    "min": 0,
                                                    "max": 13
                                                },
                                                "name": "Others"
                                            }
                                        ],
                                        "position": 0,
                                        "enabled": True
                                    },
                                    "18.75 - 24.00": {
                                        "rules": [
                                            {
                                                "filter": [
                                                    "&&",
                                                    [
                                                        ">=",
                                                        "style_exp",
                                                        "18.75"
                                                    ],
                                                    [
                                                        "<=",
                                                        "style_exp",
                                                        "24.00"
                                                    ]
                                                ],
                                                "symbolizers": [
                                                    {
                                                        "strokeWidth": 3,
                                                        "color": "#053061",
                                                        "fillOpacity": 1,
                                                        "kind": "Mark",
                                                        "wellKnownName": "Circle",
                                                        "radius": 5,
                                                        "strokeColor": "#555555",
                                                        "strokeOpacity": 1
                                                    },
                                                    {
                                                        "rotate": 0,
                                                        "size": 12,
                                                        "color": "#000000",
                                                        "offset": [
                                                            0,
                                                            0
                                                        ],
                                                        "kind": "Text",
                                                        "haloColor": "#EEEEEE",
                                                        "label": "label_exp",
                                                        "opacity": 1,
                                                        "enabled": False,
                                                        "font": [
                                                            "Roboto Light"
                                                        ],
                                                        "haloWidth": 0
                                                    }
                                                ],
                                                "scaleDenominator": {
                                                    "min": 0,
                                                    "max": 13
                                                },
                                                "name": "18.75 - 24.00"
                                            }
                                        ],
                                        "position": 4,
                                        "enabled": True
                                    },
                                    "5.00 - 8.00": {
                                        "rules": [
                                            {
                                                "filter": [
                                                    "&&",
                                                    [
                                                        ">=",
                                                        "style_exp",
                                                        "5.00"
                                                    ],
                                                    [
                                                        "<",
                                                        "style_exp",
                                                        "8.00"
                                                    ]
                                                ],
                                                "symbolizers": [
                                                    {
                                                        "strokeWidth": 3,
                                                        "color": "#e58368",
                                                        "fillOpacity": 1,
                                                        "kind": "Mark",
                                                        "wellKnownName": "Circle",
                                                        "radius": 5,
                                                        "strokeColor": "#555555",
                                                        "strokeOpacity": 1
                                                    },
                                                    {
                                                        "rotate": 0,
                                                        "size": 12,
                                                        "color": "#000000",
                                                        "offset": [
                                                            0,
                                                            0
                                                        ],
                                                        "kind": "Text",
                                                        "haloColor": "#EEEEEE",
                                                        "label": "label_exp",
                                                        "opacity": 1,
                                                        "enabled": False,
                                                        "font": [
                                                            "Roboto Light"
                                                        ],
                                                        "haloWidth": 0
                                                    }
                                                ],
                                                "scaleDenominator": {
                                                    "min": 0,
                                                    "max": 13
                                                },
                                                "name": "5.00 - 8.00"
                                            }
                                        ],
                                        "position": 1,
                                        "enabled": True
                                    },
                                    "16.00 - 18.75": {
                                        "rules": [
                                            {
                                                "filter": [
                                                    "&&",
                                                    [
                                                        ">=",
                                                        "style_exp",
                                                        "16.00"
                                                    ],
                                                    [
                                                        "<",
                                                        "style_exp",
                                                        "18.75"
                                                    ]
                                                ],
                                                "symbolizers": [
                                                    {
                                                        "strokeWidth": 3,
                                                        "color": "#6bacd1",
                                                        "fillOpacity": 1,
                                                        "kind": "Mark",
                                                        "wellKnownName": "Circle",
                                                        "radius": 5,
                                                        "strokeColor": "#555555",
                                                        "strokeOpacity": 1
                                                    },
                                                    {
                                                        "rotate": 0,
                                                        "size": 12,
                                                        "color": "#000000",
                                                        "offset": [
                                                            0,
                                                            0
                                                        ],
                                                        "kind": "Text",
                                                        "haloColor": "#EEEEEE",
                                                        "label": "label_exp",
                                                        "opacity": 1,
                                                        "enabled": False,
                                                        "font": [
                                                            "Roboto Light"
                                                        ],
                                                        "haloWidth": 0
                                                    }
                                                ],
                                                "scaleDenominator": {
                                                    "min": 0,
                                                    "max": 13
                                                },
                                                "name": "16.00 - 18.75"
                                            }
                                        ],
                                        "position": 3,
                                        "enabled": True
                                    },
                                    "8.00 - 16.00": {
                                        "rules": [
                                            {
                                                "filter": [
                                                    "&&",
                                                    [
                                                        ">=",
                                                        "style_exp",
                                                        "8.00"
                                                    ],
                                                    [
                                                        "<",
                                                        "style_exp",
                                                        "16.00"
                                                    ]
                                                ],
                                                "symbolizers": [
                                                    {
                                                        "strokeWidth": 3,
                                                        "color": "#f7f7f7",
                                                        "fillOpacity": 1,
                                                        "kind": "Mark",
                                                        "wellKnownName": "Circle",
                                                        "radius": 5,
                                                        "strokeColor": "#555555",
                                                        "strokeOpacity": 1
                                                    },
                                                    {
                                                        "rotate": 0,
                                                        "size": 12,
                                                        "color": "#000000",
                                                        "offset": [
                                                            0,
                                                            0
                                                        ],
                                                        "kind": "Text",
                                                        "haloColor": "#EEEEEE",
                                                        "label": "label_exp",
                                                        "opacity": 1,
                                                        "enabled": False,
                                                        "font": [
                                                            "Roboto Light"
                                                        ],
                                                        "haloWidth": 0
                                                    }
                                                ],
                                                "scaleDenominator": {
                                                    "min": 0,
                                                    "max": 13
                                                },
                                                "name": "8.00 - 16.00"
                                            }
                                        ],
                                        "position": 2,
                                        "enabled": True
                                    }
                                },
                                "style_col_alias": "total_no_f",
                                "style_col_name": "total_no_f",
                                "style_name": "fire style",
                                "style_type": "admin",
                                "class_type": "q",
                                "color_ramp": "RdBu",
                                "is_default_style": False,
                                "filter_type": "number",
                                "id": 395
                            },
                            {
                                "interval_count": 4,
                                "col_id": 12819,
                                "sld_name": "234_133_395_ts",
                                "json_value": {
                                    "Others": {
                                        "rules": [
                                            {
                                                "filter": [
                                                    "==",
                                                    "style_exp",
                                                    "others"
                                                ],
                                                "symbolizers": [
                                                    {
                                                        "strokeWidth": 3,
                                                        "color": "#67001f",
                                                        "fillOpacity": 1,
                                                        "kind": "Mark",
                                                        "wellKnownName": "Circle",
                                                        "radius": 5,
                                                        "strokeColor": "#555555",
                                                        "strokeOpacity": 1
                                                    },
                                                    {
                                                        "rotate": 0,
                                                        "size": 12,
                                                        "color": "#000000",
                                                        "offset": [
                                                            0,
                                                            0
                                                        ],
                                                        "kind": "Text",
                                                        "haloColor": "#EEEEEE",
                                                        "label": "label_exp",
                                                        "opacity": 1,
                                                        "enabled": False,
                                                        "font": [
                                                            "Roboto Light"
                                                        ],
                                                        "haloWidth": 0
                                                    }
                                                ],
                                                "scaleDenominator": {
                                                    "min": 0,
                                                    "max": 13
                                                },
                                                "name": "Others"
                                            }
                                        ],
                                        "position": 0,
                                        "enabled": True
                                    },
                                    "18.75 - 24.00": {
                                        "rules": [
                                            {
                                                "filter": [
                                                    "&&",
                                                    [
                                                        ">=",
                                                        "style_exp",
                                                        "18.75"
                                                    ],
                                                    [
                                                        "<=",
                                                        "style_exp",
                                                        "24.00"
                                                    ]
                                                ],
                                                "symbolizers": [
                                                    {
                                                        "strokeWidth": 3,
                                                        "color": "#053061",
                                                        "fillOpacity": 1,
                                                        "kind": "Mark",
                                                        "wellKnownName": "Circle",
                                                        "radius": 5,
                                                        "strokeColor": "#555555",
                                                        "strokeOpacity": 1
                                                    },
                                                    {
                                                        "rotate": 0,
                                                        "size": 12,
                                                        "color": "#000000",
                                                        "offset": [
                                                            0,
                                                            0
                                                        ],
                                                        "kind": "Text",
                                                        "haloColor": "#EEEEEE",
                                                        "label": "label_exp",
                                                        "opacity": 1,
                                                        "enabled": False,
                                                        "font": [
                                                            "Roboto Light"
                                                        ],
                                                        "haloWidth": 0
                                                    }
                                                ],
                                                "scaleDenominator": {
                                                    "min": 0,
                                                    "max": 13
                                                },
                                                "name": "18.75 - 24.00"
                                            }
                                        ],
                                        "position": 4,
                                        "enabled": True
                                    },
                                    "5.00 - 8.00": {
                                        "rules": [
                                            {
                                                "filter": [
                                                    "&&",
                                                    [
                                                        ">=",
                                                        "style_exp",
                                                        "5.00"
                                                    ],
                                                    [
                                                        "<",
                                                        "style_exp",
                                                        "8.00"
                                                    ]
                                                ],
                                                "symbolizers": [
                                                    {
                                                        "strokeWidth": 3,
                                                        "color": "#e58368",
                                                        "fillOpacity": 1,
                                                        "kind": "Mark",
                                                        "wellKnownName": "Circle",
                                                        "radius": 5,
                                                        "strokeColor": "#555555",
                                                        "strokeOpacity": 1
                                                    },
                                                    {
                                                        "rotate": 0,
                                                        "size": 12,
                                                        "color": "#000000",
                                                        "offset": [
                                                            0,
                                                            0
                                                        ],
                                                        "kind": "Text",
                                                        "haloColor": "#EEEEEE",
                                                        "label": "label_exp",
                                                        "opacity": 1,
                                                        "enabled": False,
                                                        "font": [
                                                            "Roboto Light"
                                                        ],
                                                        "haloWidth": 0
                                                    }
                                                ],
                                                "scaleDenominator": {
                                                    "min": 0,
                                                    "max": 13
                                                },
                                                "name": "5.00 - 8.00"
                                            }
                                        ],
                                        "position": 1,
                                        "enabled": True
                                    },
                                    "16.00 - 18.75": {
                                        "rules": [
                                            {
                                                "filter": [
                                                    "&&",
                                                    [
                                                        ">=",
                                                        "style_exp",
                                                        "16.00"
                                                    ],
                                                    [
                                                        "<",
                                                        "style_exp",
                                                        "18.75"
                                                    ]
                                                ],
                                                "symbolizers": [
                                                    {
                                                        "strokeWidth": 3,
                                                        "color": "#6bacd1",
                                                        "fillOpacity": 1,
                                                        "kind": "Mark",
                                                        "wellKnownName": "Circle",
                                                        "radius": 5,
                                                        "strokeColor": "#555555",
                                                        "strokeOpacity": 1
                                                    },
                                                    {
                                                        "rotate": 0,
                                                        "size": 12,
                                                        "color": "#000000",
                                                        "offset": [
                                                            0,
                                                            0
                                                        ],
                                                        "kind": "Text",
                                                        "haloColor": "#EEEEEE",
                                                        "label": "label_exp",
                                                        "opacity": 1,
                                                        "enabled": False,
                                                        "font": [
                                                            "Roboto Light"
                                                        ],
                                                        "haloWidth": 0
                                                    }
                                                ],
                                                "scaleDenominator": {
                                                    "min": 0,
                                                    "max": 13
                                                },
                                                "name": "16.00 - 18.75"
                                            }
                                        ],
                                        "position": 3,
                                        "enabled": True
                                    },
                                    "8.00 - 16.00": {
                                        "rules": [
                                            {
                                                "filter": [
                                                    "&&",
                                                    [
                                                        ">=",
                                                        "style_exp",
                                                        "8.00"
                                                    ],
                                                    [
                                                        "<",
                                                        "style_exp",
                                                        "16.00"
                                                    ]
                                                ],
                                                "symbolizers": [
                                                    {
                                                        "strokeWidth": 3,
                                                        "color": "#f7f7f7",
                                                        "fillOpacity": 1,
                                                        "kind": "Mark",
                                                        "wellKnownName": "Circle",
                                                        "radius": 5,
                                                        "strokeColor": "#555555",
                                                        "strokeOpacity": 1
                                                    },
                                                    {
                                                        "rotate": 0,
                                                        "size": 12,
                                                        "color": "#000000",
                                                        "offset": [
                                                            0,
                                                            0
                                                        ],
                                                        "kind": "Text",
                                                        "haloColor": "#EEEEEE",
                                                        "label": "label_exp",
                                                        "opacity": 1,
                                                        "enabled": False,
                                                        "font": [
                                                            "Roboto Light"
                                                        ],
                                                        "haloWidth": 0
                                                    }
                                                ],
                                                "scaleDenominator": {
                                                    "min": 0,
                                                    "max": 13
                                                },
                                                "name": "8.00 - 16.00"
                                            }
                                        ],
                                        "position": 2,
                                        "enabled": True
                                    }
                                },
                                "style_col_alias": "total_no_f",
                                "style_col_name": "total_no_f",
                                "style_name": "fire style",
                                "style_type": "admin",
                                "class_type": "q",
                                "color_ramp": "RdBu",
                                "is_default_style": False,
                                "filter_type": "number",
                                "id": 395
                            },
                            {
                                "interval_count": 4,
                                "col_id": 12819,
                                "sld_name": "234_133_395_ts",
                                "json_value": {
                                    "Others": {
                                        "rules": [
                                            {
                                                "filter": [
                                                    "==",
                                                    "style_exp",
                                                    "others"
                                                ],
                                                "symbolizers": [
                                                    {
                                                        "strokeWidth": 3,
                                                        "color": "#67001f",
                                                        "fillOpacity": 1,
                                                        "kind": "Mark",
                                                        "wellKnownName": "Circle",
                                                        "radius": 5,
                                                        "strokeColor": "#555555",
                                                        "strokeOpacity": 1
                                                    },
                                                    {
                                                        "rotate": 0,
                                                        "size": 12,
                                                        "color": "#000000",
                                                        "offset": [
                                                            0,
                                                            0
                                                        ],
                                                        "kind": "Text",
                                                        "haloColor": "#EEEEEE",
                                                        "label": "label_exp",
                                                        "opacity": 1,
                                                        "enabled": False,
                                                        "font": [
                                                            "Roboto Light"
                                                        ],
                                                        "haloWidth": 0
                                                    }
                                                ],
                                                "scaleDenominator": {
                                                    "min": 0,
                                                    "max": 13
                                                },
                                                "name": "Others"
                                            }
                                        ],
                                        "position": 0,
                                        "enabled": True
                                    },
                                    "18.75 - 24.00": {
                                        "rules": [
                                            {
                                                "filter": [
                                                    "&&",
                                                    [
                                                        ">=",
                                                        "style_exp",
                                                        "18.75"
                                                    ],
                                                    [
                                                        "<=",
                                                        "style_exp",
                                                        "24.00"
                                                    ]
                                                ],
                                                "symbolizers": [
                                                    {
                                                        "strokeWidth": 3,
                                                        "color": "#053061",
                                                        "fillOpacity": 1,
                                                        "kind": "Mark",
                                                        "wellKnownName": "Circle",
                                                        "radius": 5,
                                                        "strokeColor": "#555555",
                                                        "strokeOpacity": 1
                                                    },
                                                    {
                                                        "rotate": 0,
                                                        "size": 12,
                                                        "color": "#000000",
                                                        "offset": [
                                                            0,
                                                            0
                                                        ],
                                                        "kind": "Text",
                                                        "haloColor": "#EEEEEE",
                                                        "label": "label_exp",
                                                        "opacity": 1,
                                                        "enabled": False,
                                                        "font": [
                                                            "Roboto Light"
                                                        ],
                                                        "haloWidth": 0
                                                    }
                                                ],
                                                "scaleDenominator": {
                                                    "min": 0,
                                                    "max": 13
                                                },
                                                "name": "18.75 - 24.00"
                                            }
                                        ],
                                        "position": 4,
                                        "enabled": True
                                    },
                                    "5.00 - 8.00": {
                                        "rules": [
                                            {
                                                "filter": [
                                                    "&&",
                                                    [
                                                        ">=",
                                                        "style_exp",
                                                        "5.00"
                                                    ],
                                                    [
                                                        "<",
                                                        "style_exp",
                                                        "8.00"
                                                    ]
                                                ],
                                                "symbolizers": [
                                                    {
                                                        "strokeWidth": 3,
                                                        "color": "#e58368",
                                                        "fillOpacity": 1,
                                                        "kind": "Mark",
                                                        "wellKnownName": "Circle",
                                                        "radius": 5,
                                                        "strokeColor": "#555555",
                                                        "strokeOpacity": 1
                                                    },
                                                    {
                                                        "rotate": 0,
                                                        "size": 12,
                                                        "color": "#000000",
                                                        "offset": [
                                                            0,
                                                            0
                                                        ],
                                                        "kind": "Text",
                                                        "haloColor": "#EEEEEE",
                                                        "label": "label_exp",
                                                        "opacity": 1,
                                                        "enabled": False,
                                                        "font": [
                                                            "Roboto Light"
                                                        ],
                                                        "haloWidth": 0
                                                    }
                                                ],
                                                "scaleDenominator": {
                                                    "min": 0,
                                                    "max": 13
                                                },
                                                "name": "5.00 - 8.00"
                                            }
                                        ],
                                        "position": 1,
                                        "enabled": True
                                    },
                                    "16.00 - 18.75": {
                                        "rules": [
                                            {
                                                "filter": [
                                                    "&&",
                                                    [
                                                        ">=",
                                                        "style_exp",
                                                        "16.00"
                                                    ],
                                                    [
                                                        "<",
                                                        "style_exp",
                                                        "18.75"
                                                    ]
                                                ],
                                                "symbolizers": [
                                                    {
                                                        "strokeWidth": 3,
                                                        "color": "#6bacd1",
                                                        "fillOpacity": 1,
                                                        "kind": "Mark",
                                                        "wellKnownName": "Circle",
                                                        "radius": 5,
                                                        "strokeColor": "#555555",
                                                        "strokeOpacity": 1
                                                    },
                                                    {
                                                        "rotate": 0,
                                                        "size": 12,
                                                        "color": "#000000",
                                                        "offset": [
                                                            0,
                                                            0
                                                        ],
                                                        "kind": "Text",
                                                        "haloColor": "#EEEEEE",
                                                        "label": "label_exp",
                                                        "opacity": 1,
                                                        "enabled": False,
                                                        "font": [
                                                            "Roboto Light"
                                                        ],
                                                        "haloWidth": 0
                                                    }
                                                ],
                                                "scaleDenominator": {
                                                    "min": 0,
                                                    "max": 13
                                                },
                                                "name": "16.00 - 18.75"
                                            }
                                        ],
                                        "position": 3,
                                        "enabled": True
                                    },
                                    "8.00 - 16.00": {
                                        "rules": [
                                            {
                                                "filter": [
                                                    "&&",
                                                    [
                                                        ">=",
                                                        "style_exp",
                                                        "8.00"
                                                    ],
                                                    [
                                                        "<",
                                                        "style_exp",
                                                        "16.00"
                                                    ]
                                                ],
                                                "symbolizers": [
                                                    {
                                                        "strokeWidth": 3,
                                                        "color": "#f7f7f7",
                                                        "fillOpacity": 1,
                                                        "kind": "Mark",
                                                        "wellKnownName": "Circle",
                                                        "radius": 5,
                                                        "strokeColor": "#555555",
                                                        "strokeOpacity": 1
                                                    },
                                                    {
                                                        "rotate": 0,
                                                        "size": 12,
                                                        "color": "#000000",
                                                        "offset": [
                                                            0,
                                                            0
                                                        ],
                                                        "kind": "Text",
                                                        "haloColor": "#EEEEEE",
                                                        "label": "label_exp",
                                                        "opacity": 1,
                                                        "enabled": False,
                                                        "font": [
                                                            "Roboto Light"
                                                        ],
                                                        "haloWidth": 0
                                                    }
                                                ],
                                                "scaleDenominator": {
                                                    "min": 0,
                                                    "max": 13
                                                },
                                                "name": "8.00 - 16.00"
                                            }
                                        ],
                                        "position": 2,
                                        "enabled": True
                                    }
                                },
                                "style_col_alias": "total_no_f",
                                "style_col_name": "total_no_f",
                                "style_name": "fire style",
                                "style_type": "admin",
                                "class_type": "q",
                                "color_ramp": "RdBu",
                                "is_default_style": False,
                                "filter_type": "number",
                                "id": 395
                            },
                            {
                                "interval_count": None,
                                "col_id": None,
                                "sld_name": "234_133_390_ts",
                                "json_value": {
                                    "point Geometry": {
                                        "rules": [
                                            {
                                                "symbolizers": [
                                                    {
                                                        "strokeWidth": 3,
                                                        "color": "#087875",
                                                        "fillOpacity": 1,
                                                        "kind": "Mark",
                                                        "wellKnownName": "Circle",
                                                        "radius": 5,
                                                        "strokeColor": "#555555",
                                                        "strokeOpacity": 1
                                                    },
                                                    {
                                                        "rotate": 0,
                                                        "size": 12,
                                                        "color": "#000000",
                                                        "offset": [
                                                            0,
                                                            0
                                                        ],
                                                        "kind": "Text",
                                                        "haloColor": "#EEEEEE",
                                                        "label": "label_exp",
                                                        "opacity": 1,
                                                        "enabled": False,
                                                        "font": [
                                                            "Roboto Light"
                                                        ],
                                                        "haloWidth": 0
                                                    }
                                                ],
                                                "scaleDenominator": {
                                                    "min": 0,
                                                    "max": 13
                                                },
                                                "name": "point Geometry",
                                                "id": 1
                                            }
                                        ],
                                        "position": 0,
                                        "enabled": True
                                    }
                                },
                                "style_col_alias": None,
                                "style_col_name": None,
                                "style_name": "Untitled Style",
                                "style_type": "admin",
                                "class_type": None,
                                "color_ramp": "OrRd",
                                "is_default_style": True,
                                "filter_type": None,
                                "id": 390
                            }
                        ],
                        "timeseries_config": {
                            "min_value": "2023-02-13T10:51:00.190012",
                            "attribute_info": [
                                {
                                    "ts_column_id": None,
                                    "ts_column_datatype": None,
                                    "ts_style_name": None,
                                    "ts_column_alias": "Geometry",
                                    "ts_style_type": None
                                }
                            ],
                            "max_value": "2023-05-11T11:44:24.590835"
                        },
                        "cat_name": "Fire_station",
                        "isthematic": False,
                        "lyr_desc": None,
                        "label_conf": None,
                        "isanimation": False,
                        "table_name": "tbl_fire_station",
                        "layer_type": "operational",
                        "category_id": 790,
                        "geom_type": "point"
                    },
                    {
                        "style_conf": [
                            {
                                "style_col_type": "character varying",
                                "col_id": 12855,
                                "filter_type": "string",
                                "style_col_alias": "road_type",
                                "style_col_name": "road_type"
                            }
                        ],
                        "z_index": 0,
                        "doc_list": [
                            {
                                "is_popup": False,
                                "is_attribute": True,
                                "text": "sample",
                                "doc_id": 90
                            },
                            {
                                "is_popup": True,
                                "is_attribute": True,
                                "text": "ABC",
                                "doc_id": 98
                            },
                            {
                                "is_popup": True,
                                "is_attribute": True,
                                "text": "XYZ",
                                "doc_id": 112
                            }
                        ],
                        "user_style_config": [
                            {
                                "interval_count": None,
                                "col_id": None,
                                "sld_name": "234_133_392_ts",
                                "json_value": {
                                    "line Geometry": {
                                        "rules": [
                                            {
                                                "symbolizers": [
                                                    {
                                                        "cap": "round",
                                                        "color": "#0f3223",
                                                        "kind": "Line",
                                                        "width": 2,
                                                        "graphicStroke": {
                                                            "color": "#0f3223"
                                                        },
                                                        "join": "round",
                                                        "opacity": 1
                                                    },
                                                    {
                                                        "rotate": 0,
                                                        "size": 12,
                                                        "color": "#000000",
                                                        "offset": [
                                                            0,
                                                            0
                                                        ],
                                                        "kind": "Text",
                                                        "haloColor": "#EEEEEE",
                                                        "label": "label_exp",
                                                        "opacity": 1,
                                                        "enabled": False,
                                                        "font": [
                                                            "Roboto Light"
                                                        ],
                                                        "haloWidth": 0
                                                    }
                                                ],
                                                "scaleDenominator": {
                                                    "min": 0,
                                                    "max": 13
                                                },
                                                "name": "line Geometry",
                                                "id": 1
                                            }
                                        ],
                                        "position": 0,
                                        "enabled": True
                                    }
                                },
                                "style_col_alias": None,
                                "style_col_name": None,
                                "style_name": "Untitled Style",
                                "style_type": "admin",
                                "class_type": None,
                                "color_ramp": "OrRd",
                                "is_default_style": True,
                                "filter_type": None,
                                "id": 392
                            },
                            {
                                "interval_count": 4,
                                "col_id": 0,
                                "sld_name": "234_133_398_ts",
                                "json_value": {
                                    "line Geometry": {
                                        "rules": [
                                            {
                                                "symbolizers": [
                                                    {
                                                        "cap": "round",
                                                        "color": "#fb2727",
                                                        "kind": "Line",
                                                        "width": "1",
                                                        "graphicFill": {
                                                            "color": "#000000",
                                                            "wellKnownName": "none"
                                                        },
                                                        "graphicStroke": {
                                                            "color": "#9f07ed",
                                                            "wellKnownName": "none"
                                                        },
                                                        "join": "round",
                                                        "opacity": 0.4
                                                    },
                                                    {
                                                        "labelAllGroup": False,
                                                        "rotate": 0,
                                                        "color": "#000000",
                                                        "offset": [
                                                            0,
                                                            0
                                                        ],
                                                        "kind": "Text",
                                                        "haloColor": "#EEEEEE",
                                                        "label": "label_exp",
                                                        "enabled": False,
                                                        "partials": False,
                                                        "haloWidth": 0,
                                                        "followLine": False,
                                                        "size": 12,
                                                        "opacity": 1,
                                                        "font": [
                                                            "Roboto Light"
                                                        ],
                                                        "group": "no",
                                                        "conflictResolution": False
                                                    }
                                                ],
                                                "scaleDenominator": {
                                                    "min": 0,
                                                    "max": 13
                                                },
                                                "name": "line Geometry",
                                                "id": 1
                                            }
                                        ],
                                        "position": 0,
                                        "enabled": True
                                    }
                                },
                                "style_col_alias": None,
                                "style_col_name": None,
                                "style_name": "Untitled Style1",
                                "style_type": "user",
                                "class_type": "q",
                                "color_ramp": "OrRd",
                                "is_default_style": True,
                                "filter_type": None,
                                "id": 398
                            }
                        ],
                        "timeseries_config": {
                            "min_value": "2023-02-13T10:52:50.962088",
                            "attribute_info": [
                                {
                                    "ts_column_id": None,
                                    "ts_column_datatype": None,
                                    "ts_style_name": None,
                                    "ts_column_alias": "Geometry",
                                    "ts_style_type": None
                                }
                            ],
                            "max_value": "2023-05-11T16:15:57.128535"
                        },
                        "cat_name": "Road_centerline",
                        "isthematic": False,
                        "lyr_desc": None,
                        "label_conf": None,
                        "isanimation": False,
                        "table_name": "tbl_road_centerline",
                        "layer_type": "operational",
                        "category_id": 791,
                        "geom_type": "line"
                    },
                    {
                        "style_conf": [
                            {
                                "style_col_type": "numeric",
                                "col_id": 12873,
                                "filter_type": "number",
                                "style_col_alias": "shape_area",
                                "style_col_name": "shape_area"
                            }
                        ],
                        "z_index": 0,
                        "doc_list": [
                            {
                                "is_popup": True,
                                "is_attribute": True,
                                "text": "ABC",
                                "doc_id": 99
                            }
                        ],
                        "user_style_config": [
                            {
                                "interval_count": None,
                                "col_id": None,
                                "sld_name": "234_133_394_ts",
                                "json_value": {
                                    "polygon Geometry": {
                                        "rules": [
                                            {
                                                "symbolizers": [
                                                    {
                                                        "color": "#b38193",
                                                        "fillOpacity": 1,
                                                        "outlineWidth": 2,
                                                        "kind": "Fill",
                                                        "graphicFill": {
                                                            "color": "#b38193"
                                                        },
                                                        "outlineColor": "#c2a2ff",
                                                        "graphicStroke": {
                                                            "color": "#b38193"
                                                        }
                                                    },
                                                    {
                                                        "rotate": 0,
                                                        "size": 12,
                                                        "color": "#000000",
                                                        "offset": [
                                                            0,
                                                            0
                                                        ],
                                                        "kind": "Text",
                                                        "haloColor": "#EEEEEE",
                                                        "label": "label_exp",
                                                        "opacity": 1,
                                                        "enabled": False,
                                                        "font": [
                                                            "Roboto Light"
                                                        ],
                                                        "haloWidth": 0
                                                    }
                                                ],
                                                "scaleDenominator": {
                                                    "min": 0,
                                                    "max": 13
                                                },
                                                "name": "polygon Geometry",
                                                "id": 1
                                            }
                                        ],
                                        "position": 0,
                                        "enabled": True
                                    }
                                },
                                "style_col_alias": None,
                                "style_col_name": None,
                                "style_name": "Untitled Style",
                                "style_type": "admin",
                                "class_type": None,
                                "color_ramp": "OrRd",
                                "is_default_style": True,
                                "filter_type": None,
                                "id": 394
                            },
                            {
                                "interval_count": 4,
                                "col_id": 0,
                                "sld_name": "234_133_400_ts",
                                "json_value": {
                                    "polygon Geometry": {
                                        "rules": [
                                            {
                                                "symbolizers": [
                                                    {
                                                        "color": "#584c02",
                                                        "fillOpacity": 1,
                                                        "outlineWidth": "1",
                                                        "kind": "Fill",
                                                        "graphicFill": {
                                                            "color": "#eedc72",
                                                            "wellKnownName": "none"
                                                        },
                                                        "outlineColor": "#c2a2ff",
                                                        "graphicStroke": {
                                                            "color": "#eedc72",
                                                            "wellKnownName": "none"
                                                        },
                                                        "outlineOpacity": 0
                                                    },
                                                    {
                                                        "labelAllGroup": False,
                                                        "rotate": 0,
                                                        "color": "#000000",
                                                        "offset": [
                                                            0,
                                                            0
                                                        ],
                                                        "kind": "Text",
                                                        "haloColor": "#EEEEEE",
                                                        "label": "label_exp",
                                                        "enabled": False,
                                                        "partials": False,
                                                        "haloWidth": 0,
                                                        "followLine": False,
                                                        "size": 12,
                                                        "opacity": 1,
                                                        "font": [
                                                            "Roboto Light"
                                                        ],
                                                        "group": "no",
                                                        "conflictResolution": False
                                                    }
                                                ],
                                                "scaleDenominator": {
                                                    "min": 0,
                                                    "max": 13
                                                },
                                                "name": "polygon Geometry",
                                                "id": 1
                                            }
                                        ],
                                        "position": 0,
                                        "enabled": True
                                    }
                                },
                                "style_col_alias": None,
                                "style_col_name": None,
                                "style_name": "Untitled Style2",
                                "style_type": "user",
                                "class_type": "q",
                                "color_ramp": "OrRd",
                                "is_default_style": True,
                                "filter_type": None,
                                "id": 400
                            }
                        ],
                        "timeseries_config": {
                            "min_value": "2023-02-13T10:54:48.139674",
                            "attribute_info": [
                                {
                                    "ts_column_id": None,
                                    "ts_column_datatype": None,
                                    "ts_style_name": None,
                                    "ts_column_alias": "Geometry",
                                    "ts_style_type": None
                                }
                            ],
                            "max_value": "2023-05-11T12:34:45.457171"
                        },
                        "cat_name": "Slum_boundary",
                        "isthematic": False,
                        "lyr_desc": None,
                        "label_conf": None,
                        "isanimation": False,
                        "table_name": "tbl_slum_boundary",
                        "layer_type": "operational",
                        "category_id": 792,
                        "geom_type": "polygon"
                    }
                ]
            },
            "dept_name": "vmc integration department",
            "module_config": [
                {
                    "lvl": 0,
                    "module_id": 1,
                    "node_path": "1",
                    "category_id": [],
                    "isactive": True,
                    "sub_module": [],
                    "display_priority": 1,
                    "module_parent_id": None,
                    "module_name": "Layer Switcher",
                    "type": "mainleft"
                },
                {
                    "lvl": 0,
                    "module_id": 2,
                    "node_path": "2",
                    "category_id": [],
                    "isactive": True,
                    "sub_module": [
                        {
                            "lvl": 1,
                            "module_id": 16,
                            "node_path": "2.16",
                            "category_id": [],
                            "isactive": True,
                            "sub_module": [],
                            "display_priority": None,
                            "module_parent_id": 2,
                            "module_name": "Spatial Query",
                            "type": "mainleft"
                        },
                        {
                            "lvl": 1,
                            "module_id": 50,
                            "node_path": "2.50",
                            "category_id": [],
                            "isactive": True,
                            "sub_module": [],
                            "display_priority": None,
                            "module_parent_id": 2,
                            "module_name": "Attribute Query",
                            "type": "mainleft"
                        },
                        {
                            "lvl": 1,
                            "module_id": 6,
                            "node_path": "2.6",
                            "category_id": [],
                            "isactive": True,
                            "sub_module": [],
                            "display_priority": None,
                            "module_parent_id": 2,
                            "module_name": "Buffer",
                            "type": "mainleft"
                        }
                    ],
                    "display_priority": 2,
                    "module_parent_id": None,
                    "module_name": "Query Module",
                    "type": "mainleft"
                },
                {
                    "lvl": 0,
                    "module_id": 15,
                    "node_path": "15",
                    "category_id": [],
                    "isactive": True,
                    "sub_module": [],
                    "display_priority": 3,
                    "module_parent_id": None,
                    "module_name": "Attribute Table",
                    "type": "mainleft"
                },
                {
                    "lvl": 0,
                    "module_id": 17,
                    "node_path": "17",
                    "category_id": [],
                    "isactive": True,
                    "sub_module": [],
                    "display_priority": 3,
                    "module_parent_id": None,
                    "module_name": "Basemap",
                    "type": "bottomvertical"
                },
                {
                    "lvl": 0,
                    "module_id": 55,
                    "node_path": "55",
                    "category_id": [],
                    "isactive": True,
                    "sub_module": [],
                    "display_priority": 3,
                    "module_parent_id": None,
                    "module_name": "Edit Panel",
                    "type": "mainleft"
                },
                {
                    "lvl": 0,
                    "module_id": 5,
                    "node_path": "5",
                    "category_id": [],
                    "isactive": True,
                    "sub_module": [
                        {
                            "lvl": 1,
                            "module_id": 51,
                            "node_path": "5.51",
                            "category_id": [],
                            "isactive": True,
                            "sub_module": [],
                            "display_priority": None,
                            "module_parent_id": 5,
                            "module_name": "Elevation Profile",
                            "type": "mainleft"
                        },
                        {
                            "lvl": 1,
                            "module_id": 11,
                            "node_path": "5.11",
                            "category_id": [],
                            "isactive": True,
                            "sub_module": [],
                            "display_priority": 1,
                            "module_parent_id": 5,
                            "module_name": "Measure",
                            "type": "bottomvertical"
                        },
                        {
                            "lvl": 1,
                            "module_id": 13,
                            "node_path": "5.13",
                            "category_id": [
                                691
                            ],
                            "isactive": True,
                            "sub_module": [],
                            "display_priority": None,
                            "module_parent_id": 5,
                            "module_name": "Network Tracing",
                            "type": "mainleft"
                        },
                        {
                            "lvl": 1,
                            "module_id": 7,
                            "node_path": "5.7",
                            "category_id": [],
                            "isactive": True,
                            "sub_module": [
                                {
                                    "lvl": 2,
                                    "module_id": 8,
                                    "node_path": "5.7.8",
                                    "category_id": [],
                                    "isactive": True,
                                    "sub_module": [],
                                    "display_priority": None,
                                    "module_parent_id": 7,
                                    "module_name": "Basic Routing",
                                    "type": "mainleft"
                                },
                                {
                                    "lvl": 2,
                                    "module_id": 10,
                                    "node_path": "5.7.10",
                                    "category_id": [
                                        690
                                    ],
                                    "isactive": True,
                                    "sub_module": [],
                                    "display_priority": None,
                                    "module_parent_id": 7,
                                    "module_name": "Nearest Facility",
                                    "type": "mainleft"
                                }
                            ],
                            "display_priority": None,
                            "module_parent_id": 5,
                            "module_name": "Routing",
                            "type": "mainleft"
                        },
                        {
                            "lvl": 1,
                            "module_id": 70,
                            "node_path": "5.70",
                            "category_id": [],
                            "isactive": True,
                            "sub_module": [
                                {
                                    "lvl": 2,
                                    "module_id": 71,
                                    "node_path": "5.70.71",
                                    "category_id": [],
                                    "isactive": True,
                                    "sub_module": [],
                                    "display_priority": None,
                                    "module_parent_id": 70,
                                    "module_name": "Line of Sight",
                                    "type": "mainleft"
                                },
                                {
                                    "lvl": 2,
                                    "module_id": 72,
                                    "node_path": "5.70.72",
                                    "category_id": [],
                                    "isactive": True,
                                    "sub_module": [],
                                    "display_priority": None,
                                    "module_parent_id": 70,
                                    "module_name": "Viewshed",
                                    "type": "mainleft"
                                }
                            ],
                            "display_priority": 1,
                            "module_parent_id": 5,
                            "module_name": "3D Analyst",
                            "type": "bottomhorizontal"
                        },
                        {
                            "lvl": 1,
                            "module_id": 12,
                            "node_path": "5.12",
                            "category_id": [
                                292,
                                364
                            ],
                            "isactive": True,
                            "sub_module": [],
                            "display_priority": None,
                            "module_parent_id": 5,
                            "module_name": "Go To X:Y",
                            "type": "mainleft"
                        },
                        {
                            "lvl": 1,
                            "module_id": 187,
                            "node_path": "5.187",
                            "category_id": [],
                            "isactive": True,
                            "sub_module": [],
                            "display_priority": None,
                            "module_parent_id": 5,
                            "module_name": "MultiBuffer",
                            "type": "mainleft"
                        },
                        {
                            "lvl": 1,
                            "module_id": 68,
                            "node_path": "5.68",
                            "category_id": [],
                            "isactive": True,
                            "sub_module": [],
                            "display_priority": None,
                            "module_parent_id": 5,
                            "module_name": "Terrain Analysis",
                            "type": "mainleft"
                        }
                    ],
                    "display_priority": 4,
                    "module_parent_id": None,
                    "module_name": "Advanced Tools",
                    "type": "mainleft"
                },
                {
                    "lvl": 0,
                    "module_id": 14,
                    "node_path": "14",
                    "category_id": [],
                    "isactive": True,
                    "sub_module": [],
                    "display_priority": 6,
                    "module_parent_id": None,
                    "module_name": "Dashboard",
                    "type": "mainleft"
                },
                {
                    "lvl": 0,
                    "module_id": 22,
                    "node_path": "22",
                    "category_id": [],
                    "isactive": True,
                    "sub_module": [],
                    "display_priority": 7,
                    "module_parent_id": None,
                    "module_name": "PDM",
                    "type": "mainleft"
                },
                {
                    "lvl": 0,
                    "module_id": 67,
                    "node_path": "67",
                    "category_id": [],
                    "isactive": True,
                    "sub_module": [],
                    "display_priority": 8,
                    "module_parent_id": None,
                    "module_name": "Time Series",
                    "type": "mainleft"
                },
                {
                    "lvl": 0,
                    "module_id": 74,
                    "node_path": "74",
                    "category_id": [],
                    "isactive": True,
                    "sub_module": [],
                    "display_priority": 22,
                    "module_parent_id": None,
                    "module_name": "3D Button",
                    "type": "mainleft"
                },
                {
                    "lvl": 0,
                    "module_id": 221,
                    "node_path": "221",
                    "category_id": [],
                    "isactive": True,
                    "sub_module": [],
                    "display_priority": 31,
                    "module_parent_id": None,
                    "module_name": "Lidar View",
                    "type": "mainleft"
                },
                {
                    "lvl": 0,
                    "module_id": 3,
                    "node_path": "3",
                    "category_id": [],
                    "isactive": True,
                    "sub_module": [],
                    "display_priority": 35,
                    "module_parent_id": None,
                    "module_name": "Print",
                    "type": "mainright"
                },
                {
                    "lvl": 0,
                    "module_id": 229,
                    "node_path": "229",
                    "category_id": [],
                    "isactive": True,
                    "sub_module": [],
                    "display_priority": 36,
                    "module_parent_id": None,
                    "module_name": "Data Visualisation",
                    "type": "mainleft"
                },
                {
                    "lvl": 0,
                    "module_id": 251,
                    "node_path": "251",
                    "category_id": [],
                    "isactive": True,
                    "sub_module": [],
                    "display_priority": 37,
                    "module_parent_id": None,
                    "module_name": "Report Generation",
                    "type": "mainleft"
                },
                {
                    "lvl": 0,
                    "module_id": 4,
                    "node_path": "4",
                    "category_id": [],
                    "isactive": True,
                    "sub_module": [],
                    "display_priority": None,
                    "module_parent_id": None,
                    "module_name": "Bookmark",
                    "type": "mainleft"
                },
                {
                    "lvl": 0,
                    "module_id": 18,
                    "node_path": "18",
                    "category_id": [],
                    "isactive": True,
                    "sub_module": [
                        {
                            "lvl": 1,
                            "module_id": 19,
                            "node_path": "18.19",
                            "category_id": [],
                            "isactive": True,
                            "sub_module": [],
                            "display_priority": 6,
                            "module_parent_id": 18,
                            "module_name": "Zoom In",
                            "type": "bottomhorizontal"
                        },
                        {
                            "lvl": 1,
                            "module_id": 20,
                            "node_path": "18.20",
                            "category_id": [],
                            "isactive": True,
                            "sub_module": [],
                            "display_priority": 5,
                            "module_parent_id": 18,
                            "module_name": "Zoom Out",
                            "type": "bottomhorizontal"
                        },
                        {
                            "lvl": 1,
                            "module_id": 21,
                            "node_path": "18.21",
                            "category_id": [],
                            "isactive": True,
                            "sub_module": [],
                            "display_priority": 4,
                            "module_parent_id": 18,
                            "module_name": "Pan",
                            "type": "bottomhorizontal"
                        },
                        {
                            "lvl": 1,
                            "module_id": 58,
                            "node_path": "18.58",
                            "category_id": [],
                            "isactive": True,
                            "sub_module": [],
                            "display_priority": 2,
                            "module_parent_id": 18,
                            "module_name": "Information Tool",
                            "type": "bottomhorizontal"
                        },
                        {
                            "lvl": 1,
                            "module_id": 59,
                            "node_path": "18.59",
                            "category_id": [],
                            "isactive": True,
                            "sub_module": [],
                            "display_priority": 3,
                            "module_parent_id": 18,
                            "module_name": "Nav History",
                            "type": "bottomhorizontal"
                        },
                        {
                            "lvl": 1,
                            "module_id": 57,
                            "node_path": "18.57",
                            "category_id": [],
                            "isactive": True,
                            "sub_module": [],
                            "display_priority": 2,
                            "module_parent_id": 18,
                            "module_name": "Selection Tool",
                            "type": "bottomvertical"
                        }
                    ],
                    "display_priority": None,
                    "module_parent_id": None,
                    "module_name": "Basic Tools",
                    "type": "bottomvertical"
                },
                {
                    "lvl": 0,
                    "module_id": 30,
                    "node_path": "30",
                    "category_id": [],
                    "isactive": True,
                    "sub_module": [],
                    "display_priority": None,
                    "module_parent_id": None,
                    "module_name": "Free Search",
                    "type": "mainright"
                }
            ],
            "access_config": {
                "81": [
                    {
                        "access_levels": [
                            "vmc_zone",
                            "vmc_ward"
                        ],
                        "access_category_id": [
                            788,
                            789
                        ],
                        "access_id": 81,
                        "access_theme_name": "vmc_access"
                    }
                ]
            },
            "language_conf": None,
            "basemap_lyr_config": [
                {
                    "btid": 6,
                    "prj_id": 74,
                    "api_key": None,
                    "maxzoom": 20,
                    "id": 101,
                    "is_default": False,
                    "display_name": "Google Terrain Hybrid",
                    "url": "http://mt1.google.com/vt/lyrs=p&x={x}&y={y}&z={z}",
                    "minzoom": 1
                },
                {
                    "btid": 14,
                    "prj_id": 74,
                    "api_key": None,
                    "maxzoom": 20,
                    "id": 102,
                    "is_default": True,
                    "display_name": "OSM",
                    "url": "http://{a-c}.tile.openstreetmap.org/{z}/{x}/{y}.png",
                    "minzoom": 1
                },
                {
                    "btid": 2,
                    "prj_id": 74,
                    "api_key": "",
                    "maxzoom": 20,
                    "id": 112,
                    "is_default": False,
                    "display_name": "Google Satellite",
                    "url": "http://mt1.google.com/vt/lyrs=s&x={x}&y={y}&z={z}",
                    "minzoom": 1
                },
                {
                    "btid": 3,
                    "prj_id": 74,
                    "api_key": "",
                    "maxzoom": 20,
                    "id": 110,
                    "is_default": False,
                    "display_name": "Esri World Topo Map",
                    "url": "https://server.arcgisonline.com/ArcGIS/rest/services/World_Topo_Map/MapServer/tile/{z}/{y}/{x}",
                    "minzoom": 1
                },
                {
                    "btid": 4,
                    "prj_id": 74,
                    "api_key": "",
                    "maxzoom": 20,
                    "id": 111,
                    "is_default": False,
                    "display_name": "Esri World_Imagery",
                    "url": "http://server.arcgisonline.com/arcgis/rest/services/World_Imagery/MapServer/tile/{z}/{y}/{x}",
                    "minzoom": 1
                }
            ],
            "user_id": 133,
            "usertype_apptype_rel_id": 3,
            "app_types": [
                "admin_portal",
                "admin_portal",
                "admin_portal",
                "admin_portal",
                "admin_portal",
                "geo_portal"
            ],
            "default_access_id": 81,
            "dept_id": 74,
            "pivot_config": [
                {
                    "order_col": 2,
                    "category_id": 790,
                    "fk": "feat_id",
                    "org_cat_rel_id": 790,
                    "tbl_name": "mis_234.vehicle_info_1",
                    "pk": "feat_id"
                },
                {
                    "order_col": 2,
                    "category_id": 790,
                    "fk": "feat_id",
                    "org_cat_rel_id": 790,
                    "tbl_name": "mis_234.vehicle_info_1",
                    "pk": "feat_id"
                }
            ],
            "prj_config": [
                {
                    "is_jurisdictionless": False,
                    "prj_id": 103,
                    "user_id": 133,
                    "usertype_apptype_rel_id": 3,
                    "is_default": False,
                    "project_name": "p1",
                    "project_desc": ""
                },
                {
                    "is_jurisdictionless": False,
                    "prj_id": 74,
                    "user_id": 133,
                    "usertype_apptype_rel_id": 3,
                    "is_default": True,
                    "project_name": "vmc project",
                    "project_desc": "vmc project"
                }
            ]
        },
        "token": "6T46pwIa6dDj38UURKr1zLCX9W3npeNh"
    }
}


user_selection = ""
prj1 = ""
attr1 = ""
prjid = ""
category_id = ""
tbl_name = " "
updated_json = " "
category_name = " "
user_selection1 = {
    "type": "",
    "Project": "",
    "Access": "",
    "Category": "",
    "Attributes": ""
}


class ActionHandleOptions(Action):
    def name(self) -> Text:
        return "action_handle_options"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        global user_selection, prj1
   
        submenu = tracker.get_slot("submenu")
        option2action_name = {
            "main": {
                1: "action_handle_pytorch"
            },
            "pytorch_version": {
                1: ("action_get_accesses", "1"),
                2: ("action_get_accesses", "2")
            },
            "layers_version": {
                1: ("action_get_layers", "1"),
                2: ("action_get_layers", "2")
            },
            "attr_version": {
                1: ("action_get_attr", "1"),
                2: ("action_get_attr", "2"),
                3: ("action_get_attr", "3")
            },
            "report_version": {
                1: ("action_json", "1"),
                2: ("action_json", "2"),
                3: ("action_json", "3"),
                4: ("action_json", "4"),
                5: ("action_json", "5"),
                6: ("action_json", "6")
            }
        }

        try:
            option = int(tracker.get_slot("option"))
        except ValueError:
            dispatcher.utter_message(text="Please enter a number!")
            print(option)
            return [SlotSet('option', None)]

        try:
            next_action = option2action_name[submenu][option]

            user_selection = option
            # print("*******************")
            # print(user_selection)
            # print("*******************")
            # print(next_action)
            # print("*******************")
            # print(user_selection1)
            # print("*******************")

            if next_action == 'action_handle_pytorch':
                user_selection1['type'] = user_selection
            elif next_action[0] == 'action_get_accesses':
                user_selection1['Project'] = user_selection
            elif next_action[0] == 'action_get_layers':
                user_selection1['Access'] = user_selection
            elif next_action[0] == 'action_get_attr':
                user_selection1['Category'] = user_selection
            elif next_action[0] == 'action_json':
                user_selection1['Attributes'] = user_selection

            print(user_selection1)

        except KeyError:
            dispatcher.utter_message(text="This option is not available!")
            return [SlotSet('option', None)]

        if isinstance(next_action, tuple):
            return [SlotSet('option', None),
                    SlotSet('suboption', next_action[1]),
                    FollowupAction(name=next_action[0])]
        else:
            return [SlotSet('option', None),
                    FollowupAction(name=next_action)]


class GetProjectAction(Action):
    def name(self) -> Text:
        return "action_handle_pytorch"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        global config1
        if config1 is None:
            dispatcher.utter_message("Config variable is not")
            return []

        json_data = config1['data']['user_config']['prj_config']
        project_names = [obj['project_name'] for obj in json_data]
        dispatcher.utter_message(text="Please select a project:")

        for index, project_name in enumerate(project_names, start=1):
            dispatcher.utter_message(text=f"{index}. {project_name}")

        suboption = [f"{index}. {project_name}" for index,
                     project_name in enumerate(project_names, start=1)]

        return [SlotSet('submenu', "pytorch_version")] if suboption else [SlotSet('submenu', "main"), SlotSet('suboption', None)]


class GetAccessAction(Action):
    def name(self) -> Text:
        return "action_get_accesses"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        global config1, final_access
        if config1 is None:
            dispatcher.utter_message("Config variable is not")
            return []

        final_access = []
        json_data = config1['data']['user_config']['access_config']
        # access_levels = [acobj for obj in json_data for acobj in obj['access_levels']]
        objkey = json_data.keys()
        access = [acobj['access_theme_name']
                  for obj in objkey for acobj in json_data[obj]]

        for i in objkey:
            for j in json_data[i]:
                final_access.append((j['access_levels'], j['access_id']))
        print(final_access)
        if access:
            dispatcher.utter_message(text="Select any Access:")
            for index, level in enumerate(access, start=1):
                dispatcher.utter_message(text=f"{index}. {level}")

            suboption = [f"{index}. {level}" for index,
                         level in enumerate(access, start=1)]

            return [SlotSet('submenu', "layers_version")]

        else:
            dispatcher.utter_message(text="No access levels found.")

        return [SlotSet('submenu', "main"),
                    SlotSet('suboption', None)]



class GetLayersAction(Action):
    def name(self) -> Text:
        return "action_get_layers"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        global config2
        if config2 is None:
            dispatcher.utter_message("Config variable is not set")
            return []
        json_data = config2['data']['layers']
        cat_names = [obj['cat_name'] for obj in json_data]

        if cat_names:
            dispatcher.utter_message(text="Category Levels:")
            for index, level in enumerate(cat_names, start=1):
                dispatcher.utter_message(text=f"{index}. {level}")

            suboption = [f"{index}. {level}" for index,
                         level in enumerate(cat_names, start=1)]

            return [SlotSet('submenu', "attr_version")]

        else:
            dispatcher.utter_message(text="No access levels found.")

        return [SlotSet('submenu', "main"),
                    SlotSet('suboption', None)]



class FetchAndPrintColAliases(Action):
    def name(self) -> Text:
        return "action_get_attr"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        global config2

        if config2 is None:
            dispatcher.utter_message("Config variable is not")
            return []
        json_data = config2

        if 'data' in json_data and 'layers' in json_data['data']:
            layers = json_data['data']['layers']

            selected_option = tracker.latest_message['text']
            selected_layer = None

            for index, layer in enumerate(layers, start=1):
                if str(index) == selected_option:
                    selected_layer = layer
                    break

            if selected_layer:
                attributes = selected_layer.get('attributes')

                if attributes:
                    dispatcher.utter_message(text="Select any Attributes:")
                    col_aliases = [f"{index}. {attr['col_alias']}" for index, attr in enumerate(
                        attributes, start=1)]
                    print(col_aliases)
                    dispatcher.utter_message('\n'.join(col_aliases))
                    
                    slot_values = [f"{index}. {col_alias}" for index,
                                   col_alias in enumerate(col_aliases, start=1)]
                    # return [SlotSet("selected_attr", slot_values), SlotSet('suboption', None)]
                    return [SlotSet('submenu', "report_version")]

                else:
                    dispatcher.utter_message(
                        f"No attributes found for the selected layer.")
            else:
                dispatcher.utter_message(
                    f"No layer found for the selected option.")
        else:
            dispatcher.utter_message("No layers found in the response data.")

        return [SlotSet('submenu', "main"),
                    SlotSet('suboption', None)]

import requests
import json
import base64
from typing import Any, Text, Dict, List
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
import os

class UpdateJSONAction(Action):
    def name(self) -> Text:
        return "action_json"

    def run(self, dispatcher: CollectingDispatcher,tracker: Tracker,domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        global prj1, attr1, prjid, category_id, tbl_name, category_name
        prj1 = config1['data']['user_config']['prj_config'][user_selection1['Project']-1]['project_name']
        prjid = config1['data']['user_config']['prj_config'][user_selection1['Project'] - 1]['prj_id']
        category_id = config2['data']['layers'][user_selection1['Category'] - 1]['category_id']
        tbl_name = config2['data']['layers'][user_selection1['Category'] - 1]['table_name']
        category_name = config2['data']['layers'][user_selection1['Category'] - 1]['cat_name']
        category_index = user_selection1['Category'] - 1
        attribute_index = user_selection1['Attributes'] - 1
        print(tbl_name)
        print(category_index)
        print(attribute_index)

        attr1 = config2['data']['layers'][category_index]['attributes'][attribute_index]['col_alias']
        print(attr1)
        print(prjid)
        print(category_id)
        print("here")
        url = "http://192.168.20.59:8092/api/report/getDashBoardReport"

        myStaticJson = {
    "categoryId": category_id,
    "layername": tbl_name,
    "attribute": attr1,
    "extent": "298542D4353500004C2455193D2797C328187D4353500004C2477208D2797",
    "no_class": 3,
    "orgId": 234,
    "type": "distinct",
    "user_access": {
        "theme": 81,
        "vmc_zone": "",
        "vmc_ward": ""
    },
    "epsg": 32643,
    "userType": 3,
    "prjid": prjid,
    "pageLayout": "A4_portrait",
    "data": {
        "layout": "A4 Portrait",
        "srs": "EPSG:32643",
        "units": "m",
        "dpi": "56",
        "outputFilename": "mapprint",
        "outputFormat": "pdf",
        "orgImage": "234.png",
        "layers": [
            {
                "type": "OSM",
                "baseURL": "https://b.tile.openstreetmap.org",
                "singleTile": False,
                "tileSize": [
                    256,
                    256
                ],
                "maxExtent": [
                    -20037508.3392,
                    -20037508.3392,
                    20037508.3392,
                    20037508.3392
                ],
                "resolutions": [
                    156543.03390625,
                    78271.516953125,
                    39135.758475,
                    19567.8792375,
                    9783.93961875,
                    4891.969809375,
                    2445.9849046875,
                    1222.99245256282,
                    611.496226171875,
                    305.7481130859375,
                    152.87405654296876,
                    76.43702827148438,
                    38.21851413574219,
                    19.109257067871095,
                    9.554628533935547,
                    4.777314266967774,
                    2.388657133483887,
                    1.1943285667419434,
                    0.5971642833709717,
                    0.41999977320012255,
                    0.2799998488000817,
                    0.13999992440004086,
                    0.08399995464002451,
                    0.05599996976001634,
                    0.02799998488000817
                ],
                "extension": "png"
            },
            {
                "authkey": "8rt5qVm4JMK6A7lrWdd8dgDg4woP1RLW",
                "customParams": {
                    "env": "map_type:map",
                    "viewparams": "category_id:788;style_col_name:0;usertype:3;username:kushal88;cond:;gridparam:;order_col:;qrytype:0;dist:0;reverse_q:0;splfltrtype:st_intersects;refecatid:0;wkt:'';prjid:74;"
                },
                "styles": [
                    "234_132_307_ts"
                ],
                "tiled": True,
                "format": "image/png",
                "srs": "EPSG:32643",
                "layers": [
                    "citylayers4:overlay_ts_bbox_32643"
                ],
                "type": "wms",
                "name": "vmc_Zone",
                "baseURL": "http://192.168.20.59:8087/geoserver/"
            },
            {
                "authkey": "8rt5qVm4JMK6A7lrWdd8dgDg4woP1RLW",
                "customParams": {
                    "env": "map_type:map",
                    "viewparams": "category_id:789;style_col_name:0;usertype:3;username:kushal88;cond:;gridparam:;order_col:;qrytype:0;dist:0;reverse_q:0;splfltrtype:st_intersects;refecatid:0;wkt:'';prjid:74;"
                },
                "styles": [
                    "234_132_306_ts"
                ],
                "tiled": True,
                "format": "image/png",
                "srs": "EPSG:32643",
                "layers": [
                    "citylayers4:overlay_ts_bbox_32643"
                ],
                "type": "wms",
                "name": "Vmc_ward",
                "baseURL": "http://192.168.20.59:8087/geoserver/"
            },
            {
                "authkey": "8rt5qVm4JMK6A7lrWdd8dgDg4woP1RLW",
                "customParams": {
                    "time": 1684911532619,
                    "env": "map_type:map",
                    "viewparams": "category_id:790;usertype:3;username:kushal88;qrytype:0;dist:0;splfltrtype:st;wkt:'';prjid:74;user_access:{\"theme\":81\\,\"vmc_zone\":\"\"\\,\"vmc_ward\":\"\"};match:AND;gridparam: "
                },
                "styles": [
                    "234_133_390_ts"
                ],
                "tiled": True,
                "format": "image/png",
                "srs": "EPSG:32643",
                "layers": [
                    "citylayers4:overlay_ts_bbox_32643"
                ],
                "type": "wms",
                "name": "Fire_station",
                "baseURL": "http://192.168.20.59:8087/geoserver/"
            },
            {
                "type": "Vector",
                "styles": {
                    "1": {
                        "strokeColor": "#ffe085",
                        "strokeWidth": 5,
                        "fillOpacity": 0.2,
                        "fillColor": "#FFFFFF"
                    }
                },
                "name": "Measure",
                "geoJson": {
                    "type": "FeatureCollection",
                    "features": []
                },
                "styleProperty": "layer_type"
            }
        ],
        "pages": [
            {
                "mapTitle": "sf fsf fs sf scheduled",
                "comment": "sf fsf fs sf scheduled",
                "bbox": [
                    298542.4353500004,
                    2455193.2797,
                    328187.4353500004,
                    2477208.2797
                ],
                "rotation": 0
            }
        ],
        "legends": []
    },
    "url": "http://192.168.20.59:8087/geoserver/pdf/create.json?authkey=8rt5qVm4JMK6A7lrWdd8dgDg4woP1RLW"
}

        myStaticJsondumps = json.dumps(myStaticJson)

        data = myStaticJsondumps
        
        # print(data)

        headers = {
            'X-Auth-Token': '8rt5qVm4JMK6A7lrWdd8dgDg4woP1RLW',
            'Content-Type': 'application/json'
        }

        response = requests.request("POST", url, headers=headers, data=data)
        
        if response.status_code == 200:
            json_data = response.json()
            file_value = json_data.get('data', {}).get('file')
            
            if file_value:
                pdf_data = base64.b64decode(file_value)
                
                
                filename = f"{attr1}.pdf"
                file_path = os.path.join('/var/www/html/report', filename)

                # Save the PDF file
                with open(file_path, 'wb') as file:
                    file.write(pdf_data)

                # Construct the URL with dynamic filename
                file_url = f"http://demo.citylayers.in/report/{filename}"
                
                # Send the file URL as a message
                message = f"[Click here to download the file]({file_url})"
                dispatcher.utter_message(text=message)
            else:
                dispatcher.utter_message(text="Error: File value not found in the response.")
        else:
            dispatcher.utter_message(text="Error: API request failed.")

        return [SlotSet('submenu', "main"),
                    SlotSet('suboption', None)]


