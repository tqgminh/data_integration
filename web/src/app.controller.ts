import { Controller, Get, Param, Query, Res } from '@nestjs/common';
import { AppService } from './app.service';
import { Final } from './app.entity';
import { AppDto } from './app.dto';

@Controller('api/phones')
export class AppController {
  constructor(private readonly appService: AppService) {}

  @Get()
  async findAll(@Query() appDto: AppDto, @Res() res) {
    const data = await this.appService.findAll(appDto);
    res.json({ data });
  }

  @Get(':id')
  async findOne(@Param() appDto: AppDto) {
    return this.appService.findInnerJoin(appDto);
  }

  @Get('ten/:ten')
  async findByName(@Param() appDto: AppDto): Promise<Final> {
    return this.appService.findOne(appDto);
  }
}
