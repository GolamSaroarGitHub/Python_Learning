from django.shortcuts import render,redirect
from .models import Document
from .forms import DocumentForm



def home(request):

    return render(request,'home.html',{})

def model_form_upload(request):
    if request.method== 'POST':
        form=DocumentForm(request.POST,request.FILES)
        form.save()
        comarison()
        return redirect('comparison')


    else:
        form=DocumentForm()

        return render(request,'model_form_upload.html',{'form':form})




def show_difference(request):
    diff=comarison()

    return render(request,'differ.html',{'diff':diff})

def comarison():
    fname1='documents/django/comp1.txt'
    fname2='documents/django/comp2.txt'

    f1 = open(fname1)
    f2 = open(fname2)
    diff = ''
    # Print confirmation
    print("-----------------------------------")
    diff = diff + "-----------------------------------" + '\n'
    print("Comparing files ", " > " + fname1, " < " + fname2, sep='\n')
    diff = diff + "Comparing files " + '\n' + " > " + str(fname1) + '\n' + " < " + str(fname2) + '\n'
    print("-----------------------------------")
    diff = diff + "-----------------------------------" + '\n'

    # Read the first line from the files
    f1_line = f1.readline()
    f2_line = f2.readline()

    # Initialize counter for line number
    line_no = 1

    # Loop if either file1 or file2 has not reached EOF
    while f1_line != '' or f2_line != '':

        # Strip the leading whitespaces
        f1_line = f1_line.rstrip()
        f2_line = f2_line.rstrip()

        # Compare the lines from both file
        if f1_line != f2_line:

            # If a line does not exist on file2 then mark the output with + sign
            if f2_line == '' and f1_line != '':
                print(">+ ", "Line-%d" % line_no, f1_line)
                diff = diff + ">+ " + "Line-" + str(line_no) + "  " + str(f1_line)
            # otherwise output the line on file1 and mark it with > sign
            elif f1_line != '':
                print(">", "Line-%d" % line_no, f1_line)
                diff = diff + "> " "Line-" + str(line_no) + "  " + str(f1_line) + '\n'

            # If a line does not exist on file1 then mark the output with + sign
            if f1_line == '' and f2_line != '':
                print("<+", "Line-%d" % line_no, f2_line)
                diff = diff + "< " + "Line-" + str(line_no) + "  " + str(f2_line) + '\n'
            # otherwise output the line on file2 and mark it with < sign
            elif f2_line != '':
                print("<", "Line-%d" % line_no, f2_line)
                diff = diff + "< " "Line-" + str(line_no) + "  " + str(f2_line) + '\n'

            # Print a blank line
            print()
            diff = diff + '\n'

        # Read the next line from the file
        f1_line = f1.readline()
        f2_line = f2.readline()

        # Increment line counter
        line_no += 1

    # Close the files
    f1.close()
    f2.close()
    target = open('documents/django/output_diff.txt', 'w')
    print(diff)
    target.write(diff)
    return diff
