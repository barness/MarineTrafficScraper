#!/usr/bin/env bash

export PHANTOM_JS=phantomjs-2.1.1-linux-x86_64
wget https://bitbucket.org/ariya/phantomjs/downloads/$PHANTOM_JS.tar.bz2
tar xvjf $PHANTOM_JS.tar.bz2
mv $PHANTOM_JS /usr/local/share
ln -sf /usr/local/share/$PHANTOM_JS/bin/phantomjs /usr/local/bin
ln -sf /usr/local/share/$PHANTOM_JS/bin/phantomjs /usr/bin