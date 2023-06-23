from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route('/changeTextColor', methods=['POST'])
def change_text_color():
    background_color = request.json.get('backgroundColor')
    
    text_color = calculate_text_color(background_color)
    
    response = {'textColor': text_color}
    return jsonify(response)

def calculate_text_color(background_color):
    hex = background_color.lstrip('#')

    red = int(hex[0:2], 16)
    green = int(hex[2:4], 16)
    blue = int(hex[4:6], 16)

    comp_red = 255 - red
    comp_green = 255 - green
    comp_blue = 255 - blue

    complementary_hex = '#{:02x}{:02x}{:02x}' % (comp_red, comp_green, comp_blue)

    return complementary_hex

if __name__ == '__main__':
    app.run()