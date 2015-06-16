config = {
    "version": "1.0",
    "source": {
        "type": "FTP",
        "ftp": {
            "base_url": "ftp.ntsg.umt.edu",
            "data_dir": "/pub/MODIS/NTSG_Products/MOD16/MOD16A2.105_MERRAGMAO/"
        }
    },
    "processing": [
        {
            "band": 1,
            "process": [
                {
                    "extract_bands": ""
                }
            ]
        },
        {
            "band": 1,
            "output_file_name": "merge",
            "process": [
                {
                    "gdal_merge": {
                        "prefix": "gdal_merge_",
                        "extension": "tif"
                    }
                }
            ]
        },
        {
            "band": 1,
            "output_file_name": "final",
            "process": [
                {
                    "get_pixel_size" : "{{PIXEL_SIZE}}"
                },
                {
                    "gdalwarp": {
                        "opt": {
                            "-multi": "",
                            "-overwrite": "",
                            "-of": "GTiff",
                            "-s_srs": "'+proj=sinu +R=6371007.181 +nadgrids=@null +wktext'",
                            "-co": "'TILED=YES'",
                            "-t_srs": "EPSG:3857",
                            "-srcnodata": -3000,
                            "-dstnodata": -3000
                        },
                        "prefix": "gdalwarp_",
                        "extension": "tif"
                    }
                }
            ]
        },
        {
            "band": 1,
            "process": [
                {
                    "gdaladdo": {
                        "parameters": {
                            "-r": "average"
                        },
                        "overviews_levels": "2 4 8 16"
                    }
                }
            ]
        }
    ],
    "analysis": {
        "create_avg": True,
        "create_da": True,
        "stats": {
            "enable": True,
            "scripts": [
                {
                    "file": "sadc.json",
                    "description": {
                        "en": "SADC"
                    }
                }
            ]
        }
    },
    "services_base_url": "http://168.202.28.57:5005/browse/",
    "services": {
        "layers": {
            "id": "list_layers",
            "path": "modis/{product}/{year}/{day}",
            "parameters": [
                {
                    "parameter_name": "product",
                    "parameter_value": "list_products"
                },
                {
                    "parameter_name": "year",
                    "parameter_value": "list_years_from"
                },
                {
                    "parameter_name": "day",
                    "parameter_value": "$create_day_of_the_year"
                }
            ],
            "payload": {
                "fields": ["code", "label", "size"],
                "id": "code",
                "label": "label"
            },
            "description": {
                "en": "Available Layers",
                "it": "Layers Disponibili",
                "pt": "Layers Disponiveis"
            },
            "selection_type": "multiple"
        },
        "download": {
            "__type": "standard",
            "payload": {
                "filesystem_structure": {
                    "type": "object",
                    "parameters": [
                        {
                            "parameter_name": "product",
                            "parameter_value": "list_products"
                        },
                        {
                            "parameter_name": "year",
                            "parameter_value": "list_years_from"
                        },
                        {
                            "parameter_name": "day",
                            "parameter_value": "$create_day_of_the_year"
                        }
                    ]
                },
                "file_paths_and_sizes": {
                    "type": "rest_response"
                },
                "tab_id": {
                    "type": "string",
                    "parameters": [
                        "tab_",
                        "$CURRENT_INDEX"
                    ]
                }
            }
        },
        "countries": {
            "id": "list_gaul2modis",
            "path": "modis/countries",
            "parameters": [],
            "payload": {
                "fields": ["gaul_code", "gaul_label", "from_h", "to_h", "from_v", "to_v"],
                "id": "gaul_code",
                "label": "gaul_label"
            },
            "description": {
                "en": "Countries",
                "it": "Paesi",
                "pt": "Paises"
            },
            "selection_type": "multiple"
        },
        "time_range": {
            "year": "list_years_from",
            "from": "list_days_from",
            "to": "list_days_to",
            "step": 16
        },
        "filters": [
            {
                "id": "list_products",
                "path": "modis",
                "parameters": [],
                "payload": {
                    "fields": ["code", "label"],
                    "id": "code",
                    "label": "label"
                },
                "description": {
                    "en": "Available Products",
                    "it": "Prodotti Disponibili",
                    "pt": "Produtos Disponiveis"
                },
                "selection_type": "single",
                "services": [
                    {
                        "id": "list_years_from",
                        "path": "modis/{product}",
                        "parameters": [
                            {
                                "parameter_name": "product",
                                "parameter_value": "list_products"
                            }
                        ],
                        "payload": {
                            "fields": ["code", "label"],
                            "id": "code",
                            "label": "label"
                        },
                        "description": {
                            "en": "Available Years",
                            "it": "Anni Disponibili",
                            "pt": "Anos Disponiveis"
                        },
                        "selection_type": "single",
                        "services": [
                            {
                                "id": "list_days_from",
                                "path": "modis/{product}/{year}",
                                "parameters": [
                                    {
                                        "parameter_name": "product",
                                        "parameter_value": "list_products"
                                    },
                                    {
                                        "parameter_name": "year",
                                        "parameter_value": "list_years_from"
                                    }
                                ],
                                "payload": {
                                    "fields": ["code", "label"],
                                    "id": "code",
                                    "label": "label"
                                },
                                "description": {
                                    "en": "Available Days - From",
                                    "it": "Giorni Disponibili - Da",
                                    "pt": "Dias Disponiveis - Desde"
                                },
                                "selection_type": "single"
                            },
                            {
                                "id": "list_days_to",
                                "path": "modis/{product}/{year}",
                                "parameters": [
                                    {
                                        "parameter_name": "product",
                                        "parameter_value": "list_products"
                                    },
                                    {
                                        "parameter_name": "year",
                                        "parameter_value": "list_years_from"
                                    }
                                ],
                                "payload": {
                                    "fields": ["code", "label"],
                                    "id": "code",
                                    "label": "label"
                                },
                                "description": {
                                    "en": "Available Days - To",
                                    "it": "Giorni Disponibili - A",
                                    "pt": "Dias Disponiveis - Ate"
                                },
                                "selection_type": "single"
                            }
                        ]
                    }
                ]
            }
        ]
    }
}