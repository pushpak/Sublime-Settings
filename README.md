# Sublime-Settings

1. Add `subl .` command line shortcut https://www.sublimetext.com/docs/3/osx_command_line.html
```
ln -s "/Applications/Sublime Text.app/Contents/SharedSupport/bin/subl" /usr/local/bin/subl
```

2. Install font https://github.com/tonsky/FiraCode 
Install guide: macOS in the ttf folder, select all font files, click “Install font”

3. Install composer
```
curl -L https://getcomposer.org/installer -o composer-setup.php
php -r "if (hash_file('SHA384', 'composer-setup.php') === 'e115a8dc7871f15d853148a7fbac7da27d6c0030b848d9b3dc09e2a0388afed865e6a3d6b3c0fad45c48e2b5fc1196ae') { echo 'Installer verified'; } else { echo 'Installer corrupt'; unlink('composer-setup.php'); } echo PHP_EOL;"
php composer-setup.php --filename=composer --install-dir=/usr/local/bin
php -r "unlink('composer-setup.php');"
```

4. Install phpunit
```
curl -L https://phar.phpunit.de/phpunit.phar -o phpunit.phar
chmod +x phpunit.phar
sudo mv phpunit.phar /usr/local/bin/phpunit
```

5. Install php-cs-fixer https://github.com/FriendsOfPHP/PHP-CS-Fixer
```
curl -L https://github.com/FriendsOfPHP/PHP-CS-Fixer/releases/download/v1.12.1/php-cs-fixer.phar -o php-cs-fixer
sudo chmod a+x php-cs-fixer
sudo mv php-cs-fixer /usr/local/bin/php-cs-fixer
```
