STYLES = {
    "python": [
        [
            ["keyword", "\\b(lambda|return|yield|global|def|import|as|from|with|in|if|else|elif|and|or|not|is|None|True|False|while|for|try|except|pass)\\b", "orange"],
            ["function", "\\b(len|exec|eval|range|print|input|str|int|float|open|type|list|dict|set|tuple|credits|dir|copyrights|help)\\b", "purple"],
            ["number", "(\d{1,}|(?<=\d)\.)", "red"],
            ["user-function", "(?<=def\s)\w+", "blue"],
            ["string", '["\'].*?["\']', "green"],
            ["comment-single", "(?<![\\\\|\"|\'])\#.*", "red"],
        ],
        [
            ["comment-double", "'''.*'''", "green"]
        ]
    ],

    "javascript": [
        [
            ["instruction-word", "\\b(abstract|async|await|boolean|break|byte|case|catch|char|class|const|continue|debugger|default|delete|do|double|else|enum|export|extends|final|finally|float|for|function|goto|if|implements|import|in|instanceof|int|interface|let|long|native|new|null|of|package|private|protected|public|return|short|static|super|switch|synchronized|this|throw|throws|transient|try|typeof|var|void|volatile|while|with|true|false|prototype|yield)\\b", "blue"],
            ["window-instruction", "\\b(alert|all|anchor|anchors|area|assign|blur|button|checkbox|clearInterval|clearTimeout|clientInformation|close|closed|confirm|constructor|crypto|decodeURI|decodeURIComponent|defaultStatus|document|element|elements|embed|embeds|encodeURI|encodeURIComponent|escape|event|fileUpload|focus|form|forms|frame|innerHeight|innerWidth|layer|layers|link|location|mimeTypes|navigate|navigator|frames|frameRate|hidden|history|image|images|offscreenBuffering|onblur|onclick|onerror|onfocus|onkeydown|onkeypress|onkeyup|onmouseover|onload|onmouseup|onmousedown|onsubmit|open|opener|option|outerHeight|outerWidth|packages|pageXOffset|pageYOffset|parent|parseFloat|parseInt|password|pkcs11|plugin|prompt|propertyIsEnum|radio|reset|screenX|screenY|scroll|secure|select|self|setInterval|setTimeout|status|submit|taint|text|textarea|top|unescape|untaint|window)\\b", "brown"],
            ["string", "[\"'].*?[\"']", "grey"],
            ["number", "(\d{1,}|(?<=\d)[\.e])", "orange"],
            ["type-word", "\\b(Array|Date|eval|hasOwnProperty|Infinity|isFinite|isNaN|isPrototypeOf|Math|NaN|Number|Object|prototype|String|toString|undefined|valueOf)\\b", "purple"],
            ["comment-single", "(//).*", "green"],
        ],
        [
            ["comnment-double", "/\*.*\*/", "green"]
        ]
    ],

    "php": [
        [
            ["php-tags", "(<\?php|\?>)", "red,yellow"],
            ["variable", "\$\w+", "orange"],
            ["number", "(\d{1,}|(?<=\d)\.)", "red"],
            ["string", "[\"'].*?[\"']", "green"],
            ["word", "\\b(__halt_compiler|abstract|and|array|as|break|callable|case|catch|class|clone|const|continue|declare|default|die|do|echo|else|elseif|empty|enddeclare|endfor|endforeach|endif|endswitch|endwhile|eval|exit|extends|final|for|foreach|false|function|global|goto|if|implements|include|include_once|instanceof|insteadof|interface|isset|list|namespace|new|null|or|print|private|protected|public|require|require_once|return|static|switch|throw|trait|try|true|unset|use|var|while|xor|__halt_compiler|abstract|and|array|as|break|callable|case|catch|class|clone|const|continue|declare|default|die|do|echo|else|elseif|empty|enddeclare|endfor|endforeach|endif|endswitch|endwhile|eval|exit|extends|final|for|foreach|function|global|goto|if|implements|include|include_once|instanceof|insteadof|interface|isset|list|namespace|new|or|print|private|protected|public|require|require_once|return|static|switch|throw|trait|try|unset|use|var|while|xor)\\b", "blue"],
            ["constant", "\\b(__CLASS__|__DIR__|__FILE__|__FUNCTION__|__LINE__|__METHOD__|__NAMESPACE__|__TRAIT__)\\b", "blue,white,italic"],
            ["comment-single", "(//).*", "magenta,white,italic"]
        ],
        [
            ["comment-double", "/\*.*\*/", "magenta,white,italic"]
        ]
    ],

    "html": [
        [
            ["tag", "<.*?>", "blue"],
            ["arg-name", "\s\w+\=\".*?\"", "red"],
            ["arg-string", "[\"'].*?[\"']", "purple"]
        ],
        [
            ["comments", "<\!\-\-.*\-\->", "green"]
        ]
    ],

    "batch": [
        [
            ["special", "[\@]", "magenta"],
            ["keyword", "\\b(assoc|aux|break|call|cd|chcp|chdir|choice|cls|cmdextversion|color|com|com1|com2|com3|com4|con|copy|country|ctty|date|defined|del|dir|do|dpath|echo|else|endlocal|erase|errorlevel|exist|exit|for|ftype|goto|if|in|loadfix|loadhigh|lpt|lpt1|lpt2|lpt3|lpt4|md|mkdir|move|not|nul|path|pause|popd|prn|prompt|pushd|rd|rem|ren|rename|rmdir|set|setlocal|shift|start|time|title|type|ver|verify|vol)\\b", "blue"],
            ["label", ":.{1,}", "red,yellow"],
            ["variable", "(%.*?%|\!.*?\!)", "orange,white,bold"],
            ["operator", "(\=|\*|\-|\\b\/\\b|\+)", "red"]
        ],
        []
    ],

    "css": [
        [
            ["style_key", "[A-Za-z\-]+(?=:)", "grey,white,bold"],
            ["style_value", "(?=:)+;", "black"],
            ["pseudoclass", ":[:]?\w+", "orange,white,bold"],
            ["class", "\.\w+", "red"],
            ["id", "#\w+", "cyan,white,bold"],
            ["important", "!important", "red,yellow,bold"]
        ],
        [
            ["comment", "/\*.*\*/", "green"]
        ]
    ],

    "vbs": [
        [
            ["word", "\\b(addhandler|addressof|alias|and|andalso|as|boolean|by|byref|byte|byval|call|case|catch|cbool|cbyte|cchar|cdate|cdbl|cdec|char|cint|class|clng|cobj|const|continue|csbyte|cshort|csng|cstr|ctype|cuint|culng|cushort|date|decimal|declare|default|delegate|dim|directcast|do|double|each|else|elseif|end|endif|enum|erase|error|event|exit|false|finally|for|friend|function|get|gettype|global|gosub|goto|handles|if|implements|imports|in|inherits|integer|interface|is|isnot|let|lib|like|long|loop|me|mod|module|mustinherit|mustoverride|mybase|myclass|namespace|narrowing|new|next|not|nothing|notinheritable|notoverridable|object|of|on|operator|option|optional|or|orelse|out|overloads|overridable|overrides|paramarray|partial|private|property|protected|public|raiseevent|readonly|redim|rem|removehandler|resume|return|sbyte|select|set|shadows|shared|short|single|static|step|stop|strict|string|structure|sub|synclock|then|throw|to|true|try|trycast|typeof|uinteger|ulong|ushort|using|variant|wend|when|while|widening|with|withevents|writeonly|xor|attribute|begin|currency|implement|load|lset|rset|type|unload|aggregate|ansi|assembly|async|auto|await|binary|compare|custom|distinct|equals|explicit|from|group|into|isfalse|istrue|iterator|join|key|mid|off|order|preserve|skip|take|text|unicode|until|where|yield)\\b", "blue"],
            ["string", "[\"'].*[\"']", "grey"],
            ["operator", "\\b([\&\|\=\+\/\*\-])\\b", "black,white,bold"],
            ["number", "(\d{1,}|(?<=\d)[\+\.])", "red,white,bold"]
        ],
        []
    ],

    "json": [
        [
            ["brackets", "[\{\}\[\]]", "black,white,bold"],
            ["word", "\\b(false|true|null)\\b", "blue,white,bold"],
            ["number", "(\d{1,}|(?<=\d)\.)", "orange"],
            ["string", "\".*?\"", "crimson"]
        ],
        []
    ],

    "xml": [
        [
            ["tags", "<.*?>", "blue"],
            ["special_tags", "(<\?xml|\?>)", "red,yellow,bold"],
            ["attribute_names", "\w+(?=\=)", "red"],
            ["string", "\".*?\"", "purple"]
        ],
        [
            ["comment", "<\!\-\-.*\-\->", "green"]
        ]
    ],

    "htaccess": [
        [
            ["keyword", "\\b(RewriteEngine|FileETag|None|unset|ErrorDocument|Order|Deny|Allow|AuthName|AuthUser|File|AuthType|Require|Satisfy|from|deny|allow|all|Any|SSLOptions|SSLRequireSSL|SSLRequire|SSLRequire|SetEbv|ServerSignature|off|on|AddDefaultCharset|DefaultLanguage|Options|AddHandler|RemoveHandler|RewriteCond|RewriteRule|AddType|Redirect|RedirectMatch|Header|set|SetOutputFilter|SetEnvIfNoCase|Action|export|exec|DirectoryIndex|AddEncoding|ExpiresActive|ExpiresDefault)\\b", "blue"],
            ["braces", "(%\{.*?\}|\[.*?\])", "orange"],
            ["operators", "[!\^\$\=\|]", "black,white,bold"],
            ["tags", "(<.*>)", "brown"],
            ["string", "\".*\"", "purple"],
            ["comment", "#.*", "red"]
        ], []
    ],
    
    "c": [
        [
            ["preprocessor", "#.+", "brown"],
            ["instruction_word", "\\b(if|else|switch|case|default|break|goto|return|for|while|do|continue|typedef|sizeof|NULL)\\b", "blue"],
            ["type_word", "\\b(void|struct|union|enum|char|short|int|long|double|float|signed|unsigned|const|static|extern|auto|register|volatile|bool|uint8_t|uint16_t|uint32_t|uint64_t|int8_t|int16_t|int32_t|int64_t|size_t|time_t|clock_t|wchar_t|FILE)\\b", "magenta"],
            ["number", "(\d{1,}|(?<=\d)\.)", "orange"],
            ["string", "\".*\"", "grey"],
            ["comment-single", "(//).*", "green"]
        ],
        [
            ["comment-double", "/\*.*\*/)", "green"]
        ]
    ]
}






