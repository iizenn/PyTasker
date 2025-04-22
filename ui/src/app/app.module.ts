// src/app/app.module.ts
import { NgModule } from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';
import { CommonModule } from '@angular/common';
import { HttpClientModule } from '@angular/common/http';
import { ReactiveFormsModule } from '@angular/forms';
import { RouterModule } from '@angular/router';

import { AppComponent } from './app.component';
import { JobListComponent } from './job-list/job-list.component';
import { JobFormComponent } from './job-form/job-form.component';
import { routes } from './app.routes';

@NgModule({
  declarations: [AppComponent, JobListComponent, JobFormComponent],
  imports: [
    BrowserModule,
    CommonModule,
    HttpClientModule,
    ReactiveFormsModule,
    RouterModule.forRoot(routes), // ← 这里导入路由模块
  ],
  providers: [],
  bootstrap: [AppComponent],
})
export class AppModule {}
