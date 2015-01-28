<html>
<head>
</head>
<body>
    {% load extend_tags %}
    {% load extend_filters %}
    <div>
        {% var cache int=1 str="str" %}
        <p>int: {{cache.int}} {{cache.int|type}}</p>
        <p>str: {{cache.str}} {{cache.str|type}}</p>

        {% listvar cache "list" 1 2.0 "3" %}
        <p>list: {{cache.list}} {{cache.list|type}}</p>
        <p>cache: {{cache}} {{cache|type}}</p>
    </div>
</body>
</html>
