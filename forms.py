
def get_full_html(user_id):
    html_full = '<html><body>'
    html_full += '<div><form action="/api/' + user_id + '" method="POST">'
    html_full += '<p>Type a message</p><div><input name="mes_text" type="text" value="New text message"/></div>'
    html_full += '<div><br><input type="submit" value="Send"/></div>'
    html_full += '</form></div>'
    html_full += '<form action="/api/' + user_id + '" method="GET">'
    html_full += '<br><br><input type="submit" value="View message list"/></form>'
    html_full += '</body></html>'
    return html_full



