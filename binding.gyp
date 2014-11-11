{
    "targets": [
        {
            "target_name":"aminonative",
            "sources":[
                "src/base.cc",
                "src/fonts/vector.c",
                "src/fonts/vertex-buffer.c",
                "src/fonts/vertex-attribute.c",
                "src/fonts/texture-atlas.c",
                "src/fonts/texture-font.c",
                "src/fonts/shader.c",
                "src/fonts/mat4.c",

                "src/shaders.cpp",
                "src/nanojpeg.c",
                "src/upng.c",
                "src/SimpleRenderer.cpp"
            ],
            "include_dirs": [
                "src/",
                "src/fonts/",
            ],

            'conditions': [
                ['OS=="mac"', {
                    "include_dirs": [
                        " <!@(freetype-config --cflags)",
                        " <!@(pkg-config --cflags libglfw)",
                    ],
                    "libraries": [
                        " <!@(pkg-config --libs libglfw)",
                        '-framework OpenGL',
                        '-framework OpenCL',
                        '-framework IOKit',
                        '<!@(freetype-config --libs)'
                    ],
                    "sources": [
                        "src/mac.cpp",
                    ],
                    "defines": [
                        "MAC",
                        "GLFW_NO_GLU",
                        "GLFW_INCLUDE_GL3",
                    ]
                }],

                ['OS=="klaatu"', {
                    "defines": [
                        "KLAATU"
                    ]
                }],

                ['OS=="linux"', {
					"conditions" : [
	                    ["target_arch=='arm'", {
		                    "sources": [
		                        "src/rpi.cpp"
		                    ],
		                    "libraries":[
		                        "-L/opt/vc/lib/ -lbcm_host",
		                        "-lGLESv2",
		                        "-lEGL",
		                        '<!@(freetype-config --libs)',
		                    ],
		                    "defines": [
		                        "RPI"
		                    ],
		                    "include_dirs": [
		                        "/opt/vc/include/",
		                        "/usr/include/freetype2",
		                        "/opt/vc/include/interface/vcos/pthreads",
		                        "/opt/vc/include/interface/vmcs_host/linux",
		                        '<!@(freetype-config --cflags)'
		                    ]
		                }],

		                ["target_arch!='arm'", {
		                    "sources": [
		                        "src/mac.cpp"
		                    ],
		                    "libraries":[
		                        '<!@(freetype-config --libs)',
		                        "-lglfw",
		                    ],
		                    "defines": [
		                        "GL_GLEXT_PROTOTYPES",
		                        "LINUX"
		                    ],
		                    "include_dirs": [
		                        "/usr/include/freetype2",
		                        "<!@(freetype-config --cflags)"
		                    ]

		                }]
		            ]

                }]

            ]


        },
  {
      "target_name": "action_after_build",
      "type": "none",
      "dependencies": [ "<(module_name)" ],
      "copies": [
        {
          "files": [ "<(PRODUCT_DIR)/<(module_name).node" ],
          "destination": "<(module_path)"
        }
      ]
    }

    ]
}
