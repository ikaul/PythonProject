# Input: "{[hu()123]}" -> true
# Input: "{[hu(])123}" -> false
# Input: "{[hu(123}" -> false
#{sa[}] -> false

def say_hello
  puts 'Hello, World'
end

#5.times { say_hello }

#Check if a string contains balanced brackets -> {, (, [
def isBalancedString(str)
  unless str
    return true
  end
  
  stack = []
  input = str.split("")  #O(1)
  
  #Iterate via the char array to push all starting brackets {, (, [ into stack array & whenever you get a ending bracket, pop the last one from the array and check if it is the inverse of the ending bracket. 
  input.each do |ch|  #O(N -> length of str)
    if ch == "{" || ch == "[" || ch == "("
      stack.push(ch)
    elsif ch == "}" || ch == ")" || ch == "]"
      unless ( ch == "}" && stack.pop() == "{" ) || (ch == ")" && stack.pop() == "(") || (ch == "]" && stack.pop() == "[")
        return false
      end
    end
  end
  
  #check if stack is empty
  if stack.empty?
    return true
  else
    return false
  end
end 

p isBalancedString("test")
p isBalancedString("{[[test]]}")
p isBalancedString("{[[test]}}")
p isBalancedString(nil)
p isBalancedString("{[()(){test}]}")

