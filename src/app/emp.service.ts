import { Injectable } from '@angular/core';

@Injectable()
export class Empservice
{
    empDetail = [
        {id :1,name: 'abc', dep:'CSE'},
        {id :2,name: 'xyz', dep:'ECE'},
        {id :3,name: 'def', dep:'MECH'}
      ]
  getemployee() {
      return this.empDetail
    
  }
  setEmployee(emp)
  {
      this.empDetail.push(emp)
  }
}