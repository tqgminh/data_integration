import { Controller, Get, Param, Query, Res } from '@nestjs/common';
import { AppService } from './app.service';
import { App } from './app.schema';
import { AppDto } from './app.dto';

@Controller('app')
export class AppController {
  constructor(private readonly appService: AppService) {}

  @Get()
  async findAll(@Query() appDto: AppDto, @Res() res) {
    const data = await this.appService.findAll(appDto);
    res.json({ data });
  }

  @Get(':id')
  async findOne(@Param() appDto: AppDto): Promise<App> {
    return this.appService.findOne(appDto);
  }

  @Get(':name')
  async findByName(@Param() appDto: AppDto): Promise<App> {
    return this.appService.findByName(appDto);
  }
  @Get(':price')
  async findByPrice(@Param() appDto: AppDto): Promise<App> {
    return this.appService.findByPrice(appDto);
  }
  @Get(':screen')
  async findByScreen(@Param() appDto: AppDto): Promise<App> {
    return this.appService.findByScreen(appDto);
  }
  @Get(':cpu')
  async findByCpu(@Param() appDto: AppDto): Promise<App> {
    return this.appService.findByCpu(appDto);
  }
  @Get(':ram')
  async findByRam(@Param() appDto: AppDto): Promise<App> {
    return this.appService.findByRam(appDto);
  }
  @Get(':battery')
  async findByBattery(@Param() appDto: AppDto): Promise<App> {
    return this.appService.findByBattery(appDto);
  }

  @Get(':sim')
  async findBySim(@Param() appDto: AppDto): Promise<App> {
    return this.appService.findBySim(appDto);
  }
}
