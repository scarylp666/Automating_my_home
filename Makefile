ssh_command = ssh pi@192.168.1.232
ssh:
	$(ssh_command)

# Directory paths
upload          = .
remote_upload   = ~/uploaded

download        = download
remote_download = ~/to_download

ssh_upload:
	tar -cf - -C $(upload) . | $(ssh_command) "mkdir $(remote_upload) 2>/dev/null; tar -xf - -C $(remote_upload)"
ssh_download:
	mkdir $(download) 2>/dev/null
	$(ssh_command) "sudo tar -cf - -C $(remote_download) ." | tar -xf - -C $(download)
