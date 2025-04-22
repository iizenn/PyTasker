import { Component, OnInit } from '@angular/core';
import { Job, JobService } from '../services/job.service';
import { Router } from '@angular/router';

@Component({
  selector: 'app-job-list',
  standalone: false,
  templateUrl: './job-list.component.html',
  styleUrls: ['./job-list.component.scss'],
})
export class JobListComponent implements OnInit {
  jobs: Job[] = [];
  loading = true;
  error: string = '';

  constructor(private service: JobService, private router: Router) {}

  editNew() {
    this.router.navigate(['/jobs/new']);
  }

  ngOnInit(): void {
    this.load();
  }

  load(): void {
    this.loading = true;
    this.service.getAll().subscribe({
      next: (jobs) => {
        this.jobs = jobs;
        this.loading = false;
      },
      error: (err) => {
        this.error = 'Failed to load jobs.';
        this.loading = false;
      },
    });
  }

  delete(id: string) {
    if (!confirm('Delete this job?')) return;
    this.service.delete(id).subscribe(() => this.load());
  }

  edit(id: string) {
    this.router.navigate(['/jobs/edit', id]);
  }
}
