import os
import string

def sanitize_filename(s):
    """Take a string and return a valid filename constructed from the string.
Uses a whitelist approach: any characters not present in valid_chars are
removed. Also spaces are replaced with underscores.
"""
    valid_chars = "-_. %s%s" % (string.ascii_letters, string.digits)
    filename = ''.join(c for c in s if c in valid_chars)
    filename = filename.replace(' ', '_')  # I don't like spaces in filenames.
    return filename

if __name__ == '__main__':
    for fn in os.listdir('.'):
        if fn.endswith('.nii.gz'):
            os.system('mv "%s" "%s"' % (fn, sanitize_filename(fn)))
