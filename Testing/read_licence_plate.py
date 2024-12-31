# import cv2
# import string
# import easyocr
#
# # Initialize the OCR reader
# reader = easyocr.Reader(['en'], gpu=False)
#
# # Mapping dictionaries for character conversion
# dict_char_to_int = {'O': '0',
#                     'I': '1',
#                     'J': '3',
#                     'A': '4',
#                     'G': '6',
#                     'S': '5'}
#
# dict_int_to_char = {'0': 'O',
#                     '1': 'I',
#                     '3': 'J',
#                     '4': 'A',
#                     '6': 'G',
#                     '5': 'S'}
#
# def license_complies_format(text):
#     """
#     Check if the license plate text complies with the required format.
#
#     Args:
#         text (str): License plate text.
#
#     Returns:
#         bool: True if the license plate complies with the format, False otherwise.
#     """
#     if len(text) != 7:
#         return False
#
#     if (text[0] in string.ascii_uppercase or text[0] in dict_int_to_char.keys()) and \
#        (text[1] in string.ascii_uppercase or text[1] in dict_int_to_char.keys()) and \
#        (text[2] in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9'] or text[2] in dict_char_to_int.keys()) and \
#        (text[3] in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9'] or text[3] in dict_char_to_int.keys()) and \
#        (text[4] in string.ascii_uppercase or text[4] in dict_int_to_char.keys()) and \
#        (text[5] in string.ascii_uppercase or text[5] in dict_int_to_char.keys()) and \
#        (text[6] in string.ascii_uppercase or text[6] in dict_int_to_char.keys()):
#         return True
#     else:
#         return False
#
# def format_license(text):
#     """
#     Format the license plate text by converting characters using the mapping dictionaries.
#
#     Args:
#         text (str): License plate text.
#
#     Returns:
#         str: Formatted license plate text.
#     """
#     license_plate_ = ''
#     mapping = {0: dict_int_to_char, 1: dict_int_to_char, 4: dict_int_to_char, 5: dict_int_to_char, 6: dict_int_to_char,
#                2: dict_char_to_int, 3: dict_char_to_int}
#     for j in [0, 1, 2, 3, 4, 5, 6]:
#         if text[j] in mapping[j].keys():
#             license_plate_ += mapping[j][text[j]]
#         else:
#             license_plate_ += text[j]
#
#     return license_plate_
#
#
# def read_license_plate(license_plate_crop):
#     """
#     Read the license plate text from the given cropped image.
#
#     Args:
#         license_plate_crop (PIL.Image.Image): Cropped image containing the license plate.
#
#     Returns:
#         tuple: Tuple containing the formatted license plate text and its confidence score.
#     """
#
#     detections = reader.readtext(license_plate_crop)
#     print(detections)
#
#     for detection in detections:
#         bbox, text, score = detection
#
#         text = text.upper().replace(' ', '')
#
#         if license_complies_format(text):
#             return format_license(text), score
#
#     return None, None
#
# license_plate_crop = cv2.imread("D:\infosys_intern\STMS\data\ss5.png", cv2.IMREAD_COLOR)
#
# # process license plate
# license_plate_crop_gray = cv2.cvtColor(license_plate_crop, cv2.COLOR_BGR2GRAY)
# _, license_plate_crop_thresh = cv2.threshold(license_plate_crop_gray, 64, 255, cv2.THRESH_BINARY_INV)
#
# # read license plate number
# license_plate_text, license_plate_text_score = read_license_plate(license_plate_crop_thresh)
#
# print(license_plate_text, license_plate_text_score)