import { Routes } from '@angular/router';
import { JobListComponent } from './job-list/job-list.component';
import { JobFormComponent } from './job-form/job-form.component';

export const routes: Routes = [
  { path: '', redirectTo: 'jobs', pathMatch: 'full' },
  { path: 'jobs', component: JobListComponent },
  { path: 'jobs/new', component: JobFormComponent },
  { path: 'jobs/edit/:id', component: JobFormComponent },
  { path: '**', redirectTo: 'jobs' },
];
