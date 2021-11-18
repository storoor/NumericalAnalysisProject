import { Component,OnInit } from '@angular/core';
import * as parameters from '../app/numericalParameters'
import {ApiConnectionService} from './api-connection.service'

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css']
})
export class AppComponent {
  title = 'numericalAnalisis';
  parameters=parameters.parameters;
  selectedOption=0
  graph=false
  selectedMethod:any
  parameterList: string[]=[]
  responseObj: any


  constructor(private apiConnectionService:ApiConnectionService) { }

  ngOnInit(){
    this.selectedMethod=this.parameters[0]
  }

  methodSelect(){
    console.log(this.selectedOption)
     this.selectedMethod=this.parameters[this.selectedOption]
     for (var item in this.selectedMethod){
       console.log(item)
     }

     if (this.selectedMethod.key=="Grapher"){
      this.graph=true
    }

  }

  calculate(data:any){


    for (var key in data){
      var param=data[key]
      this.parameterList.push(param)
    }

    var apiObj={
      "key":this.selectedMethod.key,
      "parameters":this.parameterList
      
    }
   
    console.log(apiObj)
    var responseObj=this.apiConnectionService.runMethod(apiObj)
    responseObj.subscribe(x=>{
      this.responseObj=x
    })

    if (this.selectedMethod.key=="Grapher"){
      this.responseObj=[this.responseObj]
      console.log(this.responseObj)

    }

    this.parameterList=[]

  }
  keepOrder = (a:any, b:any) => {
    return a;
}

}
