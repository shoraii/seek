# seek
#### Учебный проект от AivanF, IQ-Beat

## Get value from key in JSON and YAML files

Usage:

        python seek.py <path_to_file> <key> [-t] [json/yaml]

Example:

`example.json`

       {
            "glossary": {
                "title": "example glossary",
                "GlossDiv": {
                    "title": "S",
                    "GlossList": {
                        "GlossEntry": {
                            "ID": "SGML",
                            "SortAs": "SGML",
                            "GlossTerm": "Standard Generalized Markup Language",
                            "Acronym": "SGML",
                            "Abbrev": "ISO 8879:1986",
                            "GlossDef": {
                                "para": "A meta-markup language, used to create markup languages such as DocBook.",
                                "GlossSeeAlso": ["GML", "XML"]
                            },
                           "GlossSee": "markup"
                        }
                    }
                }
            }
        }

`python seek.py example.json '["glossary", "GlossDiv", "title"]'`

`output:`

        INFO:root:Started seek.py
        INFO:root:Initialised logger, logging level: DEBUG
        INFO:root:Parsed arguments, got args.key = [glossary, GlossDiv, title], args.t = None
        INFO:root:file_type before checking is None
        INFO:root:file_type after checking is json
        INFO:root:Converting key argument to list...
        INFO:root:Converted key argument
        INFO:root:Opened example.json
        INFO:root:Successfully read data from example.json
        S