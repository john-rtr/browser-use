import base64


def save_screenshot(screenshot: str, path: str) -> None:
	"""Save a base64 encoded screenshot to a file.

	Args:
	screenshot (str): Base64 encoded string of the screenshot
	path (str): Path where to save the screenshot
	"""

	# Remove the data URL prefix if present (e.g., "data:image/png;base64,")
	if ',' in screenshot:
		screenshot = screenshot.split(',')[1]

	# Decode the base64 string
	image_data = base64.b64decode(screenshot)

	# Write the binary data to the file
	with open(path, 'wb') as f:
		f.write(image_data)
