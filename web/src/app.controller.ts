import { Controller, Get, Param } from '@nestjs/common';
import { AppService } from './app.service';
import { App } from './app.schema';
import { AppDto } from './app.dto';

@Controller('App')
export class AppController {
  constructor(private readonly appService: AppService) {}

  @Get()
  async findAll(): Promise<App[]> {
    return this.appService.findAll();
  }

  @Get(':id')
  async findOne(@Param() appDto: AppDto): Promise<App> {
    return this.appService.findOne(appDto);
  }

  @Get(':id')
  async findByName(@Param() appDto: AppDto): Promise<App> {
    return this.appService.findByName(appDto);
  }
  @Get(':id')
  async findByPrice(@Param() appDto: AppDto): Promise<App> {
    return this.appService.findByPrice(appDto);
  }
  @Get(':id')
  async findByScreen(@Param() appDto: AppDto): Promise<App> {
    return this.appService.findByScreen(appDto);
  }
  @Get(':id')
  async findByCpu(@Param() appDto: AppDto): Promise<App> {
    return this.appService.findByCpu(appDto);
  }
  @Get(':id')
  async findByRam(@Param() appDto: AppDto): Promise<App> {
    return this.appService.findByRam(appDto);
  }
  @Get(':id')
  async findByBattery(@Param() appDto: AppDto): Promise<App> {
    return this.appService.findByBattery(appDto);
  }

  @Get(':id')
  async findBySim(@Param() appDto: AppDto): Promise<App> {
    return this.appService.findBySim(appDto);
  }
}
