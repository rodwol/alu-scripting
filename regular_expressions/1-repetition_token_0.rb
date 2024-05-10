#!/usr/bin/env ruby
input = ARGV[0]
matches = input.scan(/hbt{2,5}n/)

# Output the matches
puts matches
