import { Component } from '@angular/core';
import { Empservice } from './emp.service';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css']
})
export class AppComponent {
  constructor(private emp: Empservice){}
  emp_id
  emp_name
  emp_dep
   myEmployee={
    id:1,
    name:'',
    dep:''
  }
  addemployee()
  {
    this.myEmployee.id=this.emp_id
    this.myEmployee.name=this.emp_name
    this.myEmployee.dep=this.emp_dep

    this.emp.setEmployee(this.myEmployee)

  }
}
