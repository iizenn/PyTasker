import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';
import { appConfig } from '../app.config';

export interface Cron {
  second?: string;
  minute?: string;
  hour?: string;
  day?: string;
  month?: string;
  day_of_week?: string;
}

export interface Job {
  id: string;
  func: string;
  args: string[];
  cron?: Cron; // 允许 cron 为 undefined
  next_run_time?: string;
}

@Injectable({ providedIn: 'root' })
export class JobService {
  private baseUrl = `${appConfig.apiBase}/tasks`;

  constructor(private http: HttpClient) {}

  /** 获取所有任务 */
  getAll(): Observable<Job[]> {
    return this.http.get<Job[]>(this.baseUrl);
  }
  /** 新建任务 */
  create(job: Job): Observable<Job> {
    return this.http.post<Job>(this.baseUrl, job);
  }
  /** 删除任务 */
  delete(id: string): Observable<void> {
    return this.http.delete<void>(`${this.baseUrl}/${id}`);
  }
}
