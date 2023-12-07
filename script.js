
function generateSummary(text, numSentences) {
 
  const sentences = text.split(/[.!?]/);

 
  const cleanedSentences = sentences
    .filter(sentence => sentence.trim() !== '')
    .map(sentence => sentence.trim());

  
  const sentenceScores = cleanedSentences.map(sentence => {
    return {
      text: sentence,
      score: sentence.split(' ').length,
    };
  });

  
  sentenceScores.sort((a, b) => b.score - a.score);

  
  const summarySentences = sentenceScores.slice(0, numSentences);

 
  const summary = summarySentences.map(sentence => sentence.text).join(' ');

  return summary;
}


const text = `
  Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed aliquet mi ut mauris iaculis, 
  eu consectetur nulla laoreet. Fusce vitae luctus tortor. Pellentesque nec eros id risus accumsan 
  suscipit. Nullam auctor urna nec elit mollis, vitae sollicitudin dolor consequat. Vivamus 
  vestibulum dui sed lorem sodales, vel aliquam enim accumsan. Donec non vestibulum tortor. 
  Integer nec purus id nisl aliquam fringilla. Curabitur vitae justo in mi aliquet fringilla. 
  Phasellus in justo et libero lacinia tincidunt eu id est. Sed volutpat pharetra mauris vitae 
  fringilla. Duis elementum lectus quis ex placerat, vitae cursus lorem bibendum. 
  Vestibulum fermentum vulputate enim, sit amet pulvinar purus lacinia vel.
`;

// Generate a summary with 2 sentences
const numSentences = 2;
const summary = generateSummary(text, numSentences);
console.log(summary);
