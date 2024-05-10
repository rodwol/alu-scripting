#!/usr/bin/env ruby
input = ARGV[0]
matches = input.scan(/hbt{1,4}n/)

# Output the matches
puts matches
