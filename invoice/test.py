#-*-encoding:utf-8-*-
import os,sys
import pytesseract
from PIL import Image
import subprocess

py_dir = os.path.dirname(os.path.realpath(__file__))
project_dir = os.path.dirname(py_dir)
myfile = project_dir+"/data/invoice/img/09089630-6405-43cg-4l28-n204ag3t5dtk.jpg"

tesseract_exe_name = 'tesseract' # Name of executable to be called at command line
scratch_image_name = "temp.bmp" # This file must be .bmp or other Tesseract-compatible format
scratch_text_name_root = "temp" # Leave out the .txt extension
cleanup_scratch_flag = True  # Temporary files cleaned up after OCR operation

def image_to_scratch(im, scratch_image_name):
    im.save(scratch_image_name, dpi=(200,200))

def call_tesseract(input_filename, output_filename):
    """Calls external tesseract.exe on input file (restrictions on types),
    outputting output_filename+'txt'"""
    #args = [tesseract_exe_name, input_filename, output_filename,'-l','chi_sim']
    args = [tesseract_exe_name, input_filename, output_filename,'-l','normal']

    proc = subprocess.Popen(args)
    retcode = proc.wait()
#    if retcode!=0:
#        errors.check_for_errors()
def image_to_string(im, cleanup = cleanup_scratch_flag):
    """Converts im to file, applies tesseract, and fetches resulting text.
    If cleanup=True, delete scratch files after operation."""
    text=""
    try:
        image_to_scratch(im, scratch_image_name)
        call_tesseract(scratch_image_name, scratch_text_name_root)
        text =retrieve_text(scratch_text_name_root)
    finally:
        if cleanup:
            perform_cleanup(scratch_image_name, scratch_text_name_root)
    return text
def	retrieve_text(scratch_text_name_root):
    inf = open(scratch_text_name_root + '.txt','r')
    text = inf.read()
    inf.close()
    return text

def perform_cleanup(scratch_image_name, scratch_text_name_root):
    """Clean up temporary files from disk"""
    for name in (scratch_image_name, scratch_text_name_root + '.txt', "tesseract.log"):
        try:
            os.remove(name)
        except OSError:
            pass
im = Image.open(myfile)
text = image_to_string(im)
print(text)