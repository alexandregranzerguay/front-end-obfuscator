from Crypto.Cipher import AES
from Crypto import Random
import glob, os
import random
import sys
import base64
import shutil


MAX_KEY_SIZE = 26
folder = '/home/alexandre/front-end-obfuscator/encrypted-files'
bootstrapClasses = ['section', 'focus', 'open', 'navbar', 'caret', 'label', 'table', 'img-responsive', 'img-rounded', 'img-thumbnail', 'img-circle', 'sr-only', 'lead', 'text-muted', 'text-primary', 'text-warning', 'text-danger', 'text-success', 'text-info', 'text-left', 'text-right', 'text-center', 'h6', 'h1', 'h2', 'h3', 'h4', 'h5', 'page-header', 'list-unstyled', 'list-inline', 'initialism', 'pull-right', 'prettyprint', 'pre-scrollable', 'container', 'row', 'col-lg-12', 'col-xs-11', 'col-xs-1', 'col-xs-2', 'col-xs-3', 'col-xs-4', 'col-xs-5', 'col-xs-6', 'col-xs-7', 'col-xs-8', 'col-xs-9', 'col-xs-10', 'col-xs-12', 'col-sm-11', 'col-sm-1', 'col-sm-2', 'col-sm-3', 'col-sm-4', 'col-sm-5', 'col-sm-6', 'col-sm-7', 'col-sm-8', 'col-sm-9', 'col-sm-10', 'col-sm-12', 'col-sm-push-1', 'col-sm-push-2', 'col-sm-push-3', 'col-sm-push-4', 'col-sm-push-5', 'col-sm-push-6', 'col-sm-push-7', 'col-sm-push-8', 'col-sm-push-9', 'col-sm-push-10', 'col-sm-push-11', 'col-sm-pull-1', 'col-sm-pull-2', 'col-sm-pull-3', 'col-sm-pull-4', 'col-sm-pull-5', 'col-sm-pull-6', 'col-sm-pull-7', 'col-sm-pull-8', 'col-sm-pull-9', 'col-sm-pull-10', 'col-sm-pull-11', 'col-sm-offset-1', 'col-sm-offset-2', 'col-sm-offset-3', 'col-sm-offset-4', 'col-sm-offset-5', 'col-sm-offset-6', 'col-sm-offset-7', 'col-sm-offset-8', 'col-sm-offset-9', 'col-sm-offset-10', 'col-sm-offset-11', 'col-md-11', 'col-md-1', 'col-md-2', 'col-md-3', 'col-md-4', 'col-md-5', 'col-md-6', 'col-md-7', 'col-md-8', 'col-md-9', 'col-md-10', 'col-md-12', 'col-md-push-0', 'col-md-push-1', 'col-md-push-2', 'col-md-push-3', 'col-md-push-4', 'col-md-push-5', 'col-md-push-6', 'col-md-push-7', 'col-md-push-8', 'col-md-push-9', 'col-md-push-10', 'col-md-push-11', 'col-md-pull-0', 'col-md-pull-1', 'col-md-pull-2', 'col-md-pull-3', 'col-md-pull-4', 'col-md-pull-5', 'col-md-pull-6', 'col-md-pull-7', 'col-md-pull-8', 'col-md-pull-9', 'col-md-pull-10', 'col-md-pull-11', 'col-md-offset-0', 'col-md-offset-1', 'col-md-offset-2', 'col-md-offset-3', 'col-md-offset-4', 'col-md-offset-5', 'col-md-offset-6', 'col-md-offset-7', 'col-md-offset-8', 'col-md-offset-9', 'col-md-offset-10', 'col-md-offset-11', 'col-lg-11', 'col-lg-1', 'col-lg-2', 'col-lg-3', 'col-lg-4', 'col-lg-5', 'col-lg-6', 'col-lg-7', 'col-lg-8', 'col-lg-9', 'col-lg-10', 'col-lg-push-0', 'col-lg-push-1', 'col-lg-push-2', 'col-lg-push-3', 'col-lg-push-4', 'col-lg-push-5', 'col-lg-push-6', 'col-lg-push-7', 'col-lg-push-8', 'col-lg-push-9', 'col-lg-push-10', 'col-lg-push-11', 'col-lg-pull-0', 'col-lg-pull-1', 'col-lg-pull-2', 'col-lg-pull-3', 'col-lg-pull-4', 'col-lg-pull-5', 'col-lg-pull-6', 'col-lg-pull-7', 'col-lg-pull-8', 'col-lg-pull-9', 'col-lg-pull-10', 'col-lg-pull-11', 'col-lg-offset-0', 'col-lg-offset-1', 'col-lg-offset-2', 'col-lg-offset-3', 'col-lg-offset-4', 'col-lg-offset-5', 'col-lg-offset-6', 'col-lg-offset-7', 'col-lg-offset-8', 'col-lg-offset-9', 'col-lg-offset-10', 'col-lg-offset-11', 'table-bordered', 'table-responsive', 'form-control', 'form-group', 'checkbox', 'checkbox-inline', 'input-sm', 'input-lg', 'control-label', 'input-group-addon', 'form-control-static', 'help-block', 'btn', 'active', 'btn-default', 'btn-primary', 'btn-warning', 'btn-danger', 'btn-success', 'btn-info', 'btn-link', 'btn-lg', 'btn-xs', 'btn-block', 'fade', 'in', 'collapse', 'collapsing', 'glyphicon', 'dropdown', 'dropdown-menu', 'divider', 'dropdown-header', 'dropdown-backdrop', 'btn-group-vertical', 'btn-group', 'dropdown-toggle', 'btn-group-justified', 'input-group', 'col', 'input-group-btn', 'nav', 'nav-divider', 'nav-tabs', 'nav-justified', 'nav-tabs-justified', 'pill-pane', 'navbar-header', 'navbar-collapse', 'navbar-static-top', 'navbar-fixed-bottom', 'navbar-fixed-top', 'navbar-brand', 'navbar-toggle', 'icon-bar', 'navbar-nav', 'navbar-left', 'navbar-right', 'navbar-form', 'navbar-btn', 'navbar-text', 'navbar-default', 'navbar-link', 'navbar-inverse', 'breadcrumb', 'pagination', 'pager', 'label-default', 'label-primary', 'label-success', 'label-info', 'label-warning', 'label-danger', 'badge', 'jumbotron', 'thumbnail', 'caption', 'alert', 'alert-link', 'alert-dismissable', 'close', 'alert-success', 'alert-info', 'alert-warning', 'alert-danger', 'progress', 'progress-bar', 'progress-bar-success', 'progress-bar-info', 'progress-bar-warning', 'progress-bar-danger', 'media-body', 'media', 'media-object', 'media-heading', 'pull-left', 'media-list', 'list-group', 'list-group-item', 'list-group-item-heading', 'list-group-item-text', 'panel', 'panel-body', 'panel-heading', 'panel-title', 'panel-footer', 'panel-default', 'panel-primary', 'panel-success', 'panel-warning', 'panel-danger', 'panel-info', 'well', 'well-lg', 'well-sm', 'modal-open', 'modal', 'modal-dialog', 'modal-content', 'modal-backdrop', 'modal-header', 'modal-title', 'modal-body', 'modal-footer', 'tooltip', 'top', 'right', 'bottom', 'left', 'tooltip-inner', 'tooltip-arrow', 'popover', 'popover-title', 'popover-content', 'arrow', 'carousel', 'carousel-inner', 'item', 'prev', 'next', 'carousel-control', 'glyphicon-chevron-right', 'icon-next', 'carousel-indicators', 'carousel-caption', 'hide', 'show', 'invisible', 'text-hide', 'affix', 'hidden', 'visible-xs', 'visible-sm', 'visible-md', 'visible-lg', 'hidden-xs', 'hidden-sm', 'hidden-md', 'hidden-lg', 'visible-print', 'hidden-print']


def main():
    # user_input = raw_input("what is the name of the file (with extension)")  #use raw_input for python 2.X or input for python 3.X
    # mode = getMode()
    # key = getKey()

    #This will wipe the directory at which files are written
    for the_file in os.listdir(folder):
        file_path = os.path.join(folder, the_file)
        try:
            if os.path.isfile(file_path):
                os.unlink(file_path)
                # elif os.path.isdir(file_path): shutil.rmtree(file_path)
        except Exception as e:
            print(e)

    key = raw_input('enter a password')
    files = [f for f in os.listdir('.') if os.path.isfile(f)]
    # files = ["app.js", "Alexandre Granzer-Guay.php"] #Use this if you only want to work with one file (must use two files for the loop to work though)
    for f in files:
        if "LICENSE" in f or "README" in f:
            continue
        filename, extension = f.split(".")
        print(filename, extension)
        # Determine the extension of the file.
        if 'php' in extension:
            f2 = filename + "_encrypted.php"
            f = filename + ".php"
            print(f, f2)
            PHPclassSelector(f, f2, key)
        elif 'js' in extension:
            f2 = filename + "_encrypted.js"
            f = filename + ".js"
            print(f, f2)
            JSclassSelector(f, f2, key)
        elif 'css' in extension:
            f2 = filename + "_encrypted.css"
            f = filename + ".css"
            print(f, f2)
            CSSclassSelector(f, f2, key)


def encode(key, string):
    encoded_chars = []
    for i in xrange(len(string)):
        key_c = key[i % len(key)]
        encoded_c = chr(ord(string[i]) + ord(key_c) % 256)
        encoded_chars.append(encoded_c)
    encoded_string = "".join(encoded_chars)
    return base64.urlsafe_b64encode(encoded_string).encode("hex")


def PHPclassSelector(document, document2, key):
    flag = 0
    f = open(document, "r")
    f2 = open(os.path.join(folder, document2), "w")
    for line in f:
        # Check for embedded scripts
        if flag is 1:
            line = JSclassSelectorForPHP(line, key)
        if "<script>" in line:
            flag = 1
            line = JSclassSelectorForPHP(line, key)
        if "class" in line and flag is 0:
            print(line)
            words = PHPclassStripper(line)
            # if "section" in words:
            #     pass
            if "glyphicon" not in words:
                for word in words:
                    if word not in bootstrapClasses:
                        en_word = encode(key, word)
                        line = line.replace(word, en_word)
                        print("not encrypted class name:" + word)
                        print("encrypted class name:" + en_word)
                        print("changed line:" + line)
        # Once it is the end of embedded script, lower the flag
        if "</script>" in line:
            flag = 0
        f2.write(line)
    f2.close()
    print("done changing class names")
    f2 = open(os.path.join(folder, document2), "r")
    print(f2.read())


def PHPclassStripper(line):
    new_string = line.split("class", 1)[1]
    try:
        new_string = new_string.split("\"", 1)[1]
    except:
        pass
    try:
        new_string = new_string.split("\"", 1)[0]
    except:
        pass
    words = new_string.split()
    return words


def JSclassSelectorForPHP(line, key):
    if "(\"." in line:        #add in new class names
        print(line)
        flag = 0
        word = JSclassStripper(line, flag)
        # print("word list:" + words)
        en_word = encode(key, word)
        line = line.replace(word, str(en_word))     #arg 2 needs to be a string not bytes
        print("not encrypted class name:" + word)
        print("encrypted class name:", en_word)    #changed "+" to "," can't add bytes and strings
        print("changed line:" + line)
    elif "(\'." in line:
        print(line)
        flag = 1
        word = JSclassStripper(line, flag)
        # print("word list:" + words)
        en_word = encode(key, word)
        line = line.replace(word, str(en_word))  # arg 2 needs to be a string not bytes
        print("not encrypted class name:" + word)
        print("encrypted class name:", en_word)  # changed "+" to "," can't add bytes and strings
        print("changed line:" + line)
    if "Class" in line:
        print(line)
        flag = 2
        word = JSclassStripper(line, flag)
        # print("word list:" + words)
        en_word = encode(key, word)
        line = line.replace(word, str(en_word))  # arg 2 needs to be a string not bytes
        print("not encrypted class name:" + word)
        print("encrypted class name:", en_word)  # changed "+" to "," can't add bytes and strings
        print("changed line:" + line)
    return line


def JSclassSelector(document, document2, key):
    words = []                                          #we have an array of words to be replaced that is checked on every line
    print('Entered JS Class selector')
    f = open(document, "r")
    f2 = open(os.path.join(folder, document2), "w")
    for line in f:
        if "(\"." in line:        #add in new class names
            print(line)
            flag = 0
            word = JSclassStripper(line, flag)
            # print("word list:" + words)
            en_word = encode(key, word)
            line = line.replace(word, str(en_word))     #arg 2 needs to be a string not bytes
            print("not encrypted class name:" + word)
            print("encrypted class name:", en_word)    #changed "+" to "," can't add bytes and strings
            print("changed line:" + line)
        elif "(\'." in line:
            print(line)
            flag = 1
            word = JSclassStripper(line, flag)
            # print("word list:" + words)
            en_word = encode(key, word)
            line = line.replace(word, str(en_word))  # arg 2 needs to be a string not bytes
            print("not encrypted class name:" + word)
            print("encrypted class name:", en_word)  # changed "+" to "," can't add bytes and strings
            print("changed line:" + line)
        if "Class" in line:
            print(line)
            flag = 2
            word = JSclassStripper(line, flag)
            # print("word list:" + words)
            en_word = encode(key, word)
            line = line.replace(word, str(en_word))  # arg 2 needs to be a string not bytes
            print("not encrypted class name:" + word)
            print("encrypted class name:", en_word)  # changed "+" to "," can't add bytes and strings
            print("changed line:" + line)
        f2.write(line)
    f2.close()
    print("done changing class names")
    f2 = open(os.path.join(folder, document2), "r")
    print(f2.read())


def JSclassStripper(line, flag):
    if flag is 0:
        print('Entered JS class stripper')
        print(line)
        new_string = line.split("\".", 1)[1]
        print(new_string)
        className = new_string.split("\"", 1)[0]
        print("selected class name is:" + className)
    elif flag is 1:
        print('Entered JS class stripper')
        print(line)
        new_string = line.split("\'.", 1)[1]
        print(new_string)
        className = new_string.split("\'", 1)[0]
        print("selected class name is:" + className)
    elif flag is 2:
        print('Entered JS class stripper')
        print(line)
        try:
            new_string = line.split("ass(\"", 1)[1]
            print(new_string)
            className = new_string.split("\"", 1)[0]
        except:
            new_string = line.split("ass(\'", 1)[1]
            print(new_string)
            className = new_string.split("\'", 1)[0]
        print("selected class name is:" + className)
    return className


def CSSclassSelector(document, document2, key):
    f = open(document, "r")
    f2 = open(os.path.join(folder, document2), "w")
    for line in f:
        if "." in line:
            print(line)
            words = CSSclassStripper(line)
            if "glyphicon" not in words:
                for word in words:
                    if ":" in word:
                        word = word.split(":")[0]
                    if "," in word:
                        word = word.split(",")[0]
                    if word not in bootstrapClasses and "\"" not in word:
                        en_word = encode(key, word)
                        toReplace = "."+word                            #was running into issues with ".h1" replacing "h1" also
                        willReplace = "."+str(en_word)
                        line = line.replace(toReplace, willReplace, 1)
                        print("not encrypted class name:" + word)
                        print("encrypted class name:" , en_word)
                        print("changed line:" + line)
        f2.write(line)
    f2.close()
    print("done changing class names")
    f2 = open(os.path.join(folder, document2), "r")
    print(f2.read())


def CSSclassStripper(line):
    words = []
    new_string = line.split(".")
    _ = new_string.pop(0)
    for each in new_string:
        if len(each) != 0 and each[0].isalpha():            #check that there is a letter after the '.'
            print("TO BE APPENDED: " + each.split()[0])
            words.append(each.split()[0])                   #append the class name to words
    return words


if __name__ == "__main__":
    main()



