def shift_color(hex_color, brightness_offset=20):
    """
    Shift the brightness of a given hex color code by a specified offset.

    - Parameters:
        - hex_color (str): The hex color code to be shifted.
        - brightness_offset (int): The offset value to shift the brightness. Positive values make the color brighter, 
                                   while negative values make it darker. Default is 20.

    - Returns:
        - shifted_color (str): The hex color code after shifting the brightness.
    """
    rgb_hex = [ hex_color[x : x + 2] for x in [1, 3, 5] ]
    
    if int(rgb_hex[0], 16) < brightness_offset and int(rgb_hex[1], 16) < brightness_offset and int(rgb_hex[2], 16) < brightness_offset:
        new_rgb_int = [ int(hex_value, 16) + 2 * brightness_offset for hex_value in rgb_hex ]
    else:
        new_rgb_int = [ int(hex_value, 16) - brightness_offset for hex_value in rgb_hex ]
        
    new_rgb_int = [min([255, max([0, i])]) for i in new_rgb_int]
    return "#" + "".join(['0' + hex(i)[2:] if len(hex(i)[2:]) < 2 else hex(i)[2:] for i in new_rgb_int])