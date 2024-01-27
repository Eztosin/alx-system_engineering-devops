# Increase hard file limit for user holberton
sudo sed -i '/holberton hard/s/5/50000/' /etc/security/limits.conf

# Increase soft file limit for user holberton
sudo sed -i '/holberton soft/s/4/50000/' /etc/security/limits.conf
