import { Component, OnInit, ElementRef } from '@angular/core';
import { BackserviceService } from './backservice.service';
import { HttpClient } from '@angular/common/http';
import { User } from './user';
import { Crop } from './crop';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css']
})
export class AppComponent implements OnInit {
  
  
  public crop : Crop = new Crop;

  public u : User[]= [{name:"vinit",address:"Pune"},{name:"patil",address:"Pune"}];
  public u1 : User = {name:"patil",address:"Pune"};
  constructor(private back : BackserviceService,private httpClient: HttpClient,private elementRef:ElementRef)
  {
    //this.sayHi();
  }

  ngOnInit(): void {
    
  }

  ngAfterViewInit(){
    this.elementRef.nativeElement.ownerDocument.body.style.backgroundColor = '#117a65';
 }

  sayHi() {
    console.log(this.u);
    this.httpClient.get('http://127.0.0.1:5000/employee').subscribe(data => {
      console.log(data[0]["objects"]);
      for(let i in data[0])
      {
        console.log(data[0][i])
      }
    })
  }

  public OnSubmit()
  {
    this.httpClient.post('http://127.0.0.1:5000/employee',this.crop).subscribe(data => {
      console.log(data);
    })
  }

}
