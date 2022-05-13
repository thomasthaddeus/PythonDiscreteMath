get_data_headers():
title =input('Enter a title for the
data:'</strong>)
print('You entered:
{}'</strong>.format(title))
headerOne=input('\nEnter the column 1
header: '</strong>)
print('You entered:
{}'</strong>.format(headerOne))
headerTwo=input('\nEnter the column 2
header: '</strong>)
print('You entered:
{}'</strong>.format(headerTwo))
return</strong>
[title,headerOne,headerTwo]

def get_data_points():
    data_point_dict={}
    while True</strong>:

        data=input('Enter a data point (-1 to stop input):
            if data==-1 then
=='-1'</strong>:
&nbsp;&nbsp;
break
&nbsp;elif ',' not in</strong>
data:
&nbsp;print('Error:
No comma in string.\n'</strong>)
&nbsp;elif</strong>
data.count(','</strong>)&gt;1:
&nbsp;&nbsp;
print('Error: Too many commas in input.\n'</strong>)
&nbsp;
else</strong>:
&nbsp;&nbsp;
data=data.split(','</strong>)
&nbsp;&nbsp;
try</strong>:

data_point_dict[data[0].strip()] = int(data[1])

print('Data string: {}'</strong>.format(data[0]))

print('Data integer: {}'</strong>.format(data[1]))

&nbsp;&nbsp;
except</strong>:

print('Error: Comma not followed by an
integer.\n'</strong>)
return</strong> data_point_dict


def</strong> print_data(header,data_points):

print('{0:^50}'</strong>.format(header[0]))

print('{0:&lt;24}{1:^1}{2:&gt;25}'</strong>.format(header[1],'|'</strong>,header[2]))
print('='</strong>*50)
for</strong> key,value
in</strong> data_points.items():
&nbsp;
print('{0:&lt;24}{1:^1}{2:&gt;25}'</strong>.format(key,'|'</strong>,value))

def</strong> print_histogram(data_points):
print('\n\n'</strong>)
for</strong> key,value
in</strong> data_points.items():
&nbsp;
print('{0:&lt;24}
{1}'</strong>.format(key,'*'</strong>*value))

def</strong> main():
headers=get_data_headers()
data_points=get_data_points()
print_data(headers,data_points)
print_histogram(data_points)

main()

<em>========================================================================================</em></p>