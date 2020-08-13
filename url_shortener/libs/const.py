import string


# 62 = (uppercase + lowercase + digits)
# math.pow(62,5) = 916132832
BASIC_CHARS = "".join([string.ascii_uppercase, string.ascii_lowercase, string.digits])

PATH_LENGTH = 5
