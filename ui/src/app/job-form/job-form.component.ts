import { Component, OnInit } from '@angular/core';
import { FormBuilder, FormGroup, Validators } from '@angular/forms';
import { ActivatedRoute, Router } from '@angular/router';
import { JobService, Job } from '../services/job.service';

@Component({
  selector: 'app-job-form',
  standalone: false,
  templateUrl: './job-form.component.html',
  styleUrls: ['./job-form.component.scss'],
})
export class JobFormComponent implements OnInit {
  form!: FormGroup;
  loading = false;
  error = '';
  isEdit = false;
  jobId = '';

  constructor(
    private fb: FormBuilder,
    private route: ActivatedRoute,
    public router: Router,
    private jobService: JobService
  ) {}

  ngOnInit(): void {
    this.jobId = this.route.snapshot.paramMap.get('id') || '';
    this.isEdit = !!this.jobId;

    this.form = this.fb.group({
      id: [this.jobId, Validators.required],
      func: ['run_script', Validators.required],
      args: ['', Validators.required],
      cron: this.fb.group({
        second: ['*/10', Validators.required],
        minute: [''],
        hour: [''],
        day: [''],
        month: [''],
        day_of_week: [''],
      }),
    });

    // 可选：如果是编辑页并想自动填充，可以加上 getAll() + filter，但你没实现 getById，就跳过了
  }

  onSubmit(): void {
    if (this.form.invalid) return;

    this.loading = true;
    this.error = '';

    const raw = this.form.value;

    const payload: Job = {
      id: raw.id,
      func: raw.func,
      args: raw.args.split(',').map((a: string) => a.trim()),
      cron: raw.cron,
    };

    this.jobService.create(payload).subscribe({
      next: () => this.router.navigate(['/jobs']),
      error: () => {
        this.error = '保存失败';
        this.loading = false;
      },
    });
  }
}
