# PLOT HISTOGRAM WITH ALIGNMENT AND VALUES
def plot_histogram( show_value = True,**kwargs):
    spacing = 0
    design = kwargs.get('design')
    if design =="":
        design ="===== "
    alignment = kwargs.get('alignment')
   
    if(alignment):
        spacing = max(dict.values())

    for key,value in dict.items():
        print(f' {key} | ', end = '')
        i = 0

        while i < value:
            print(f'{design}',end='')
            i += 1

        if(show_value):
            print(f'{value}'.rjust((spacing-value)*len(design)+1))

        print()

dict = {2:6,1:3, 9:2,4:3,3:1}
plot_histogram(design='+++++ ',alignment=True, show_value=True)