#!/usr/bin/env ruby
#Matches 10 digit phone number
puts ARGV[0].scan(/(^\d{10,12})/).join
