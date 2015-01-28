<html>
<head>
</head>
<body>
    {% load extend_filters %}
    <h2>Hello {{ "world"|oruser }}</h2>
</body>
</html>
