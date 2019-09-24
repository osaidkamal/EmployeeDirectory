import { Component, OnInit } from '@angular/core';
import { Empservice } from '../emp.service';

@Component({
  selector: 'app-emp-details',
  templateUrl: './emp-details.component.html',
  styleUrls: ['./emp-details.component.css']
})
export class EmpDetailsComponent implements OnInit {

  constructor(private emp: Empservice) { }

  ngOnInit() {
    this.empDetail=this.emp.getemployee()
  }
  empDetail = [ ]
  getemployee()
  {
    return this.empDetail
  }
}
