import python

from Value len, CallNode call
where len.getName() = "len" and len.getACall() = call
select call.getLocation()

