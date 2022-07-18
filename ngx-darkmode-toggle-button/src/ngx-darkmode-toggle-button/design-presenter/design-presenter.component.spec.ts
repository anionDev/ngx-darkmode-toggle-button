import { ComponentFixture, TestBed } from '@angular/core/testing';

import { DesignPresenterComponent } from './design-presenter.component';

describe('DesignPresenterComponent', () => {
  let component: DesignPresenterComponent;
  let fixture: ComponentFixture<DesignPresenterComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ DesignPresenterComponent ]
    })
    .compileComponents();

    fixture = TestBed.createComponent(DesignPresenterComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
