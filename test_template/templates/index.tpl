<html>
<head>
</head>
<body>
    {% load extend_tags %}
    {% load extend_filters %}
    <h2>Hello {% random_choice "world" ""|oruser "noname"|oruser %}</h2>
</body>
</html>
