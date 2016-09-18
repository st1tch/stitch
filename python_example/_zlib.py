import zlib

#compress
_input = open('my_log_file', 'rb').read()
_output = zlib.compress(_input, 9)  #9 is level
f = open('compressed_file', 'wb')
f.write(_output)
f.close()


#decompress
_input = open('abc.zlib', 'rb').read()
_output = zlib.decompress(_input)
f = open('my_recovered_log_file', 'wb')
f.write(_output)
f.close()
