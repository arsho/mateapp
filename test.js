function calculateHiddenDigits(firstNumber, secondNumber){
  for(let i=1;i<=9;i++){
    let current = i*100 + firstNumber;
    for(let j=1;j<=9;j++){
      let second_number = j*10 + secondNumber;
      let product = first_number * second_number;
      product = product.toString();
      if(product.length== 5 && product[0]=="5" && product[4]==4){
        console.log(first_number, second_number, product);
      }
    }
  }
}

calculateHiddenDigits(62, 7);