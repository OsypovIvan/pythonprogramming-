from django.http import HttpResponse


def my_info(request):
    html = """
    <html>
    <head>
        <title>Моя інформація</title>
        <style>
            table {
                border-collapse: collapse;
                width: 50%;
                margin: 50px auto;
                font-family: Arial, sans-serif;
            }
            th, td {
                border: 1px solid #333;
                padding: 10px;
                text-align: left;
            }
            th {
                background-color: #f2f2f2;
            }
            h2 {
                text-align: center;
            }
        </style>
    </head>
    <body>
        <h2>Інформація про мене</h2>
        <table>
            <tr><th>Поле</th><th>Значення</th></tr>
            <tr><td>Ім'я</td><td>Іван Осипов</td></tr>
            <tr><td>Професія</td><td>Junior programmer</td></tr>
            <tr><td>Місце роботи</td><td>Київ (City)</td></tr>
            <tr><td>Хобі</td><td>Backend developer</td></tr>
        </table>
    </body>
    </html>
    """
    return HttpResponse(html)
