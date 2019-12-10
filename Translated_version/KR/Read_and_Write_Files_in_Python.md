## Read and Write Files in Python


- Open a File in read+ mode(Opens file for reading and writing)
```
   target=open('filename.txt','r+')
```

- Print the file content
```
  print target.read()
```
- Write content into the filename

```
  target.write("I m writing into the file \n")
```

- There are also other other modes to access files. They are, 
<table class="table table-bordered">
<tr>
<td class="ts">1</td>
<td><p><b>r</b></p>
<p>Opens a file for reading only. The file pointer is placed at the beginning of the file. This is the default mode.</p></td>
</tr>
<tr>
<td class="ts">2</td>
<td><p><b>rb</b></p>
<p>Opens a file for reading only in binary format. The file pointer is placed at the beginning of the file. This is the default mode.</p></td>
</tr>
<tr>
<td class="ts">3</td>
<td><p><b>r+</b></p>
<p>Opens a file for both reading and writing. The file pointer placed at the beginning of the file.</p></td>
</tr>
<tr>
<td class="ts">4</td>
<td><p><b>rb+</b></p>
<p>Opens a file for both reading and writing in binary format. The file pointer placed at the beginning of the file.</p></td>
</tr>
<tr>
<td class="ts">5</td>
<td><p><b>w</b></p>
<p>Opens a file for writing only. Overwrites the file if the file exists. If the file does not exist, creates a new file for writing.</p></td>
</tr>
<tr>
<td class="ts">6</td>
<td><p><b>wb</b></p>
<p>Opens a file for writing only in binary format. Overwrites the file if the file exists. If the file does not exist, creates a new file for writing.</p></td>
</tr>
<tr>
<td class="ts">7</td>
<td><p><b>w+</b></p>
<p>Opens a file for both writing and reading. Overwrites the existing file if the file exists. If the file does not exist, creates a new file for reading and writing.</p></td>
</tr> 
<tr>
<td class="ts">8</td>
<td><p><b>wb+</b></p>
<p>Opens a file for both writing and reading in binary format. Overwrites the existing file if the file exists. If the file does not exist, creates a new file for reading and writing.</p></td>
</tr>
<tr>
<td class="ts">9</td>
<td><p><b>a</b></p>
<p>Opens a file for appending. The file pointer is at the end of the file if the file exists. That is, the file is in the append mode. If the file does not exist, it creates a new file for writing.</p></td>
</tr> 
<tr>
<td class="ts">10</td>
<td><p><b>ab</b></p>
<p>Opens a file for appending in binary format. The file pointer is at the end of the file if the file exists. That is, the file is in the append mode. If the file does not exist, it creates a new file for writing.</p></td>
</tr> 
<tr>
<td class="ts">11</td>
<td><p><b>a+</b></p>
<p>Opens a file for both appending and reading. The file pointer is at the end of the file if the file exists. The file opens in the append mode. If the file does not exist, it creates a new file for reading and writing.</p></td>
</tr> 
<tr>
<td class="ts">12</td>
<td><p><b>ab+</b></p>
<p>Opens a file for both appending and reading in binary format. The file pointer is at the end of the file if the file exists. The file opens in the append mode. If the file does not exist, it creates a new file for reading and writing.</p></td>
</tr>
</table>
