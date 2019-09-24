import { Component, OnInit } from '@angular/core';
import { Empservice } from '../emp.service';

@Component({
  selector: 'app-emp-list',
  templateUrl: './emp-list.component.html',
  styleUrls: ['./emp-list.component.css']
})
export class EmpListComponent implements OnInit {
  

  constructor(private emp:Empservice) { }

  ngOnInit() {
    this.empDetail=this.emp.getemployee()
  }
  empDetail = [ ]
 
  getemployee()
  {
    return this.empDetail
  }

}
