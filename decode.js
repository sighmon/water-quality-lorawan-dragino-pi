function Decode(fPort, bytes, variables) {
  var decoded = {};
  if (fPort === 1) {
    var stringFromBytes = String.fromCharCode.apply(String, bytes);
    var allReadings = stringFromBytes.split('|');
    for (var i = 0; i < allReadings.length; i++) {
      var readingArray = allReadings[i].split(':');
      decoded[readingArray[0]] = String(readingArray[1]);
    }
  }
  return decoded;
}
