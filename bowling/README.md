## Bowling
From https://www.linuxtopia.org/online\_books/programming\_books/python\_programming/python\_ch40.html . Changed the strike notation to X\_.


Bowling is played in ten frames, each of which allows one or two deliveries. If all ten pins are bowled over in the first delivery, there is no second delivery.

Each frame has a score based on the delivery in that frame, as well as the next one or two deliveries. This means that the score for a frame may not necessarily be posted at the end of the frame. It also means that the tenth frame may require a total of three deliveries to resolve the scoring.

- __Rule A.__ The score for a frame is the total pins bowled over during that frame, if the number is less than ten (an open frame, or error or split depending some other rules beyond the scope of this problem).
- __Rule B.__ If all ten pins are bowled over on the first delivery (a strike), the score for that frame is 10 + the next two deliveries.
- __Rule C.__ If all ten pins are bowled over between the first two deliveries (a spare), the score for that frame is 10 + the next delivery.

A game can be as few as twelve deliveries: ten frames plus two additional deliveries in the tenth frame to resolve the rule B scoring. A game can be as many as twenty deliveries: ten open frames of less than 10 pins bowled over during the frame.

There is a relatively straight-forward annotation for play. Each frame has two characters to describe the pins bowled during the delivery. The final frame has three characters for a total of 21 characters.

Rule A: If the frame is open, the two characters are the two deliveries; the total will be less than 10. If a delivery fails to bowl over any pins, a - is used instead of a number.

Rule B: If the frame is strike, the two characters are X\_. No second delivery was made.

Rule C: If the frame is a spare, the first character is the number of pins on the first delivery. The second character is a /.

For example:

8/9-X\_X\_6/4/X␣8-X\_XXX

Results in a score of 194.
