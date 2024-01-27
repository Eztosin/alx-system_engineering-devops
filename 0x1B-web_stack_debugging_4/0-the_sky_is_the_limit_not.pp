# Increase the ULIMIT of the default file
sudo sed -i 's/15/4096/' /etc/default/nginx

# Restart Nginx
sudo systemctl restart nginx
